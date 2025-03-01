use ratatui::widgets::{TableState};
use regex::Regex;
use rusqlite::{Connection, Result};
use std::io::{self, BufRead, Read};
use std::process::Stdio;
use std::{error, fs, vec};
use sysinfo::System;
use tokio::process::Command;
use tokio::io::AsyncBufReadExt;
use prost::Message;
use std::fs::{File};
use std::path::{Path, PathBuf};

/// Application result type.
pub type AppResult<T> = std::result::Result<T, Box<dyn error::Error>>;

const DATABASE_FILE: &str = "../../../storage/database.sqlite";
pub const LOG_FILE: &str = "../../../storage/app.log";
pub const ENV_FILE: &str = "../../../.env";
const SERVICES_ROOT: &str = "../../../storage/__registry__";
const METADATA_ROOT: &str = "../../../storage/__metadata__";
pub const RAM_TIMES: usize = 500;
pub const CPU_TIMES: usize = 500;

pub mod protos {
    include!(concat!("protos", "/celaut.rs"));
}

trait Identifiable {
    fn id(&self) -> &str;
}

#[derive(Debug, Clone)]
pub struct IdentifiableString(pub String);

impl Identifiable for IdentifiableString {
    fn id(&self) -> &str {
        &self.0
    }
}

#[derive(Debug)]
pub struct Peer {
    pub id: String,
    pub uri: String,
    pub gas: String,
    pub rpi: Option<String>  // Reputation proof id
}

impl Identifiable for Peer {
    fn id(&self) -> &str {
        &self.id
    }
}

#[derive(Debug)]
pub struct Service {
    pub id: String,
    pub tag: String
}

impl Identifiable for Service {
    fn id(&self) -> &str {
        &self.id
    }
}

#[derive(Debug)]
pub struct Client {
    pub id: String,
    pub gas: String
}

impl Identifiable for Client {
    fn id(&self) -> &str {
        &self.id
    }
}

#[derive(Debug)]
pub struct Container {
    pub id: String,
    pub ip: String,
    pub gas: String
}

impl Identifiable for Container {
    fn id(&self) -> &str {
        &self.id
    }
}

#[derive(Debug)]
pub struct Env {
    pub id: String,
    pub value: String,
    pub info: String,
    pub group: String,
}

impl Identifiable for Env {
    fn id(&self) -> &str {
        &self.id
    }
}

#[derive(Debug)]
pub struct Tunnel {
    pub id: String,
    pub uri: String,
    pub service: String,
    pub live: bool,
}

impl Identifiable for Tunnel {
    fn id(&self) -> &str {
        &self.id
    }
}

fn get_peers() -> Result<Vec<Peer>> {
    Ok(Connection::open(DATABASE_FILE)?
        .prepare(
            "SELECT p.id, u.ip, u.port, p.gas_mantissa, p.gas_exponent, p.reputation_proof_id
                FROM peer p
                JOIN slot s ON p.id = s.peer_id
                JOIN uri u ON s.id = u.slot_id",
        )?
        .query_map([], |row| {
            let id: String = row.get(0)?;
            let ip: String = row.get(1)?;
            let port: u16 = row.get(2)?;
            let gas_mantissa: i64 = row.get(3)?;
            let gas_exponent: i32 = row.get(4)?;
            let rpi: Option<String> = row.get(5)?;

            let gas_value = gas_mantissa as f64 * 10f64.powi(gas_exponent as i32);
            let gas = format!("{:e}", gas_value);

            Ok(Peer {
                id,
                uri: format!("{}:{}", ip, port),
                gas,
                rpi, // Assign the optional reputation_proof_id
            })
        })?
        .collect::<Result<Vec<Peer>>>()?)
}

fn get_clients() -> Result<Vec<Client>> {
    Ok(Connection::open(DATABASE_FILE)?
        .prepare("SELECT id, gas_mantissa, gas_exponent FROM clients")?
        .query_map([], |row| {
            let id: String = row.get(0)?;
            let gas_mantissa: i64 = row.get(1)?;
            let gas_exponent: i32 = row.get(2)?;

            let gas_value = gas_mantissa as f64 * 10f64.powi(gas_exponent as i32);
            let gas = format!("{:e}", gas_value);

            Ok(Client {
                id,
                gas,
            })
        })?
        .collect::<Result<Vec<Client>>>()?)
}

fn get_instances() -> Result<Vec<Container>> {
    let conn = Connection::open(DATABASE_FILE)?;

    let internal_instances = conn
        .prepare("SELECT id, ip, gas_mantissa, gas_exponent FROM internal_services")?
        .query_map([], |row| {
            let id: String = row.get(0)?;
            let ip: String = row.get(1)?;

            let gas_mantissa: i64 = row.get(2)?;
            let gas_exponent: i32 = row.get(3)?;

            let gas_value = gas_mantissa as f64 * 10f64.powi(gas_exponent as i32);
            let gas = format!("{:e}", gas_value);

            Ok(Container {
                id, ip, gas 
            })
        })?
        .collect::<Result<Vec<Container>>>()?;

    /*let external_instances = conn
        .prepare("SELECT token FROM external_services")?
        .query_map([], |row| {
            let id: String = row.get(0)?;
            Ok(Container { id })
        })?
        .collect::<Result<Vec<Container>>>()?;
    */

    let mut instances = Vec::new();
    instances.extend(internal_instances);
    // instances.extend(external_instances);

    Ok(instances)
}

fn get_services() -> Result<Vec<Service>, io::Error> {
    // Read all entries in the SERVICES_ROOT directory
    let entries = fs::read_dir(Path::new(SERVICES_ROOT))?;
    let mut services = Vec::new();

    for entry in entries {
        let entry = entry?;
        let path = entry.file_name();
    
        // Convert the file name to a string
        let service_id = path.to_string_lossy().into_owned();
    
        // Construct the metadata file path
        let metadata_path = PathBuf::from(METADATA_ROOT).join(&service_id);
    
        let mut tag = String::from("any");
    
        // Check if the metadata file exists
        if metadata_path.exists() {
            // Wrap the metadata processing in a Result handling block
            tag = match (|| -> Result<String, Box<dyn std::error::Error>> {
                // Open the metadata file
                let mut file = File::open(&metadata_path)?;
                let mut buf = Vec::new();
    
                // Read the metadata file into the buffer
                file.read_to_end(&mut buf)?;
    
                // Decode the protobuf message from the buffer
                let metadata: protos::Metadata = protos::Metadata::decode(&*buf)?;
    
                let result_tag = if let Some(hashtag) = metadata.hashtag {
                    if !hashtag.tag.is_empty() {
                        hashtag.tag.first().cloned()
                    } else {
                        Some(String::from("No tags found in hashtag"))
                    }
                } else {
                    Some(String::from("No hashtag found in metadata"))
                };
    
                Ok(result_tag.unwrap_or_else(|| String::from("No tag available")))
            })() {
                Ok(t) => t,
                Err(e) => format!("{}", e)
            };
        }
    
        // Push the service into the vector
        services.push(Service { id: service_id, tag: tag });
    }

    Ok(services)
}

fn get_envs() -> Result<Vec<Env>, io::Error> {
    let path = Path::new(ENV_FILE);
    let file = fs::File::open(&path)?;
    let reader = io::BufReader::new(file);

    let lines: Vec<String> = reader.lines().collect::<Result<_, _>>()?;
    let mut envs = Vec::new();
    let mut current_group = String::new();

    let mut iter = lines.iter().peekable();
    while let Some(line) = iter.next() {
        let line = line.trim();

        if line.starts_with("# ----") {
            if let Some(group_line) = iter.next() {
                if group_line.trim().starts_with("# ") {
                    current_group = group_line.trim_start_matches("# ").to_string();
                }
            }
            continue;
        }

        if line.is_empty() || line.starts_with('#') {
            continue;
        }

        if let Some((key, value_with_comment)) = line.split_once('=') {
            let (value, info) = if let Some((val, comment)) = value_with_comment.split_once('#') {
                (val.trim().to_string(), comment.trim().to_string())
            } else {
                (value_with_comment.trim().to_string(), String::new())
            };

            envs.push(Env {
                id: key.trim().to_string(),
                value: value.trim().to_string(),
                info: info,
                group: current_group.clone(),
            });
        }
    }

    Ok(envs)
}

fn get_tunnels() -> Result<Vec<Tunnel>> {
    Ok(Connection::open(DATABASE_FILE)?
        .prepare("SELECT id, uri, service, live FROM tunnels")?
        .query_map([], |row| {
            let id: String = row.get(0)?;
            let uri: String = row.get(1)?;
            let service: String = row.get(2)?;
            let live: bool = row.get(3)?;
            Ok(Tunnel {
                id,
                uri,
                service,
                live,
            })
        })?
        .collect::<Result<Vec<Tunnel>>>()?)
}


fn get_ram_usage(sys: &mut System) -> u64 {
    // First we update all information of our system struct.
    sys.refresh_memory();

    // Get total and used memory
    let total_memory = sys.total_memory();
    let used_memory = sys.used_memory();

    // Calculate the RAM usage in percentage
    let ram_usage_percentage = (used_memory as f64 / total_memory as f64) * 100.0;
    ram_usage_percentage as u64
}

fn get_cpu_usage(sys: &mut System) -> u64 {
    // Refresh CPU information
    sys.refresh_cpu();

    // Retrieve CPU usage as a percentage for all CPUs combined
    let cpu_usage_percentage = sys.global_cpu_info().cpu_usage();

    cpu_usage_percentage as u64
}

#[derive(Debug)]
pub struct TabsState<'a> {
    pub titles: Vec<&'a str>,
    pub index: usize,
}

impl<'a> TabsState<'a> {
    pub fn new(titles: Vec<&'a str>) -> TabsState {
        TabsState { titles, index: 0 }
    }

    pub fn next(&mut self) {
        self.index = (self.index + 1) % self.titles.len();
    }

    pub fn previous(&mut self) {
        if self.index > 0 {
            self.index -= 1;
        } else {
            self.index = self.titles.len() - 1;
        }
    }
}

#[derive(Debug)]
pub struct StatefulList<T: Identifiable> {
    pub state: TableState,
    pub state_id: Option<String>,
    pub items: Vec<T>,
}

impl<T: Identifiable> StatefulList<T> {
    pub fn with_items(items: Vec<T>) -> Self {
        Self {
            state: TableState::default(),
            state_id: None,
            items,
        }
    }

    pub fn refresh(&mut self, items: Vec<T>) {
        self.items = items;
        // Reset the state if the list is empty
        if self.items.is_empty() {
            self.state.select(None);
            self.state_id = None;
        }
    }

    pub fn next(&mut self) {
        if self.items.is_empty() {
            self.state.select(None);
            self.state_id = None;
            return;
        }

        let i = match self.state.selected() {
            Some(i) => {
                if i >= self.items.len() - 1 {
                    0
                } else {
                    i + 1
                }
            }
            None => 0,
        };
        self.state.select(Some(i));
        self.state_id = Some(self.items[i].id().to_string());
    }

    pub fn previous(&mut self) {
        if self.items.is_empty() {
            self.state.select(None);
            self.state_id = None;
            return;
        }

        let i = match self.state.selected() {
            Some(i) => {
                if i == 0 {
                    self.items.len() - 1
                } else {
                    i - 1
                }
            }
            None => 0,
        };
        self.state.select(Some(i));
        self.state_id = Some(self.items[i].id().to_string());
    }
}

/// Application.
#[derive(Debug)]
pub struct App<'a> {
    pub title: &'a str,
    pub tabs: TabsState<'a>,
    pub running: bool,
    pub logs: Vec<String>,
    pub peers: StatefulList<Peer>,
    pub clients: StatefulList<Client>,
    pub instances: StatefulList<Container>,
    pub services: StatefulList<Service>,
    pub envs: StatefulList<Env>,
    pub tunnels: StatefulList<Tunnel>,
    pub ram_usage: Vec<u64>,
    pub cpu_usage: Vec<u64>,
    pub sys: System,
    pub mode_view_index: StatefulList<IdentifiableString>,
    pub block_view_index: StatefulList<IdentifiableString>,
    pub connect_popup: bool,
    pub connect_text: String,
}

impl<'a> Default for App<'a> {
    fn default() -> Self {
        Self {
            title: "NODO TUI",
            tabs: TabsState::new(vec!["PEERS", "CLIENTS", "INSTANCES", "SERVICES", "ENVS", "TUNNELS"]),
            running: true,
            logs: Vec::new(),
            peers: StatefulList::with_items(get_peers().unwrap_or_default()),
            clients: StatefulList::with_items(get_clients().unwrap_or_default()),
            instances: StatefulList::with_items(get_instances().unwrap_or_default()),
            services: StatefulList::with_items(get_services().unwrap_or_default()),
            envs: StatefulList::with_items(get_envs().unwrap_or_default()),
            tunnels: StatefulList::with_items(get_tunnels().unwrap_or_default()),
            ram_usage: [0; RAM_TIMES].to_vec(),
            cpu_usage: [0; CPU_TIMES].to_vec(),
            sys: System::new_all(),
            mode_view_index: StatefulList::with_items(
                vec!["", "10", "10-10", "10-10-10", "20-10", "30"]
                    .into_iter()
                    .map(|s| IdentifiableString(s.to_string()))
                    .collect(),
            ),
            block_view_index: StatefulList::with_items(
                vec!["ram-usage", "cpu-usage", "tui-logs", "logs"]
                    .into_iter()
                    .map(|s| IdentifiableString(s.to_string()))
                    .collect(),
            ),
            connect_popup: false,
            connect_text: "".to_string(),
        }
    }
}

impl<'a> App<'a> {
    /// Constructs a new instance of [`App`].
    pub fn new() -> Self {
        Self::default()
    }

    pub fn on_right(&mut self) {
        self.tabs.next();
    }

    pub fn on_left(&mut self) {
        self.tabs.previous();
    }

    pub fn on_up(&mut self) {
        match self.tabs.index {
            0 => self.peers.previous(),
            1 => self.clients.previous(),
            2 => self.instances.previous(),
            3 => self.services.previous(),
            4 => self.envs.previous(),
            5 => self.tunnels.previous(),
            _ => {}
        }
    }

    pub fn on_down(&mut self) {
        match self.tabs.index {
            0 => self.peers.next(),
            1 => self.clients.next(),
            2 => self.instances.next(),
            3 => self.services.next(),
            4 => self.envs.next(),
            5 => self.tunnels.next(),
            _ => {}
        }
    }

    pub fn next_block_view(&mut self) {
        self.block_view_index.next();
    }

    pub fn previous_block_view(&mut self) {
        self.block_view_index.previous();
    }

    pub fn change_mode_view(&mut self) {
        self.mode_view_index.next();
    }

    /// Handles the tick event of the terminal.
    pub fn tick(&self) {}

    /// Set running to false to quit the application.
    pub fn quit(&mut self) {
        self.running = false;
    }

    pub fn open_popup(&mut self) {
        self.connect_popup = true;
    }

    pub fn close_popup(&mut self) {
        self.connect_popup = false;
    }

    async fn execute_command(&mut self, args: Vec<String>) -> io::Result<()> {
        const COMMAND: &str = "nodo";
        let mut child = Command::new(COMMAND)
            .args(&args)
            .stdout(Stdio::piped())
            .stderr(Stdio::piped())
            .spawn()?;

        let stdout = child.stdout.take().expect("Failed to capture stdout");
        let stderr = child.stderr.take().expect("Failed to capture stderr");

        let mut stdout_reader = tokio::io::BufReader::new(stdout).lines();
        let mut stderr_reader = tokio::io::BufReader::new(stderr).lines();

        while let Some(line) = stdout_reader.next_line().await? {
            self.logs.push(format!("STDOUT: {}", line));
        }

        while let Some(line) = stderr_reader.next_line().await? {
            self.logs.push(format!("STDERR: {}", line));
        }

        let status = child.wait().await?;
        self.logs.push(format!("Command exited with status: {}", status));

        Ok(())
    }

    pub async fn connect(&mut self) {
        if !self.connect_text.is_empty() {
            let re = Regex::new(
                    r"^.*:\d{1,5}$"
                ).unwrap();
            if re.is_match(&self.connect_text) {
                let args = vec!["connect".to_string(), self.connect_text.clone()];
                self.execute_command(args).await;
                self.connect_text.clear();
                self.close_popup();
            } // TODO else show error msg during 3 seconds or any key press.
        }
    }

    pub async fn press_d(&mut self) {
        match self.tabs.index {
            0 => {}
            1 => {}
            2 => {}
            3 => {}
            _ => {}
        }
    }

    pub async fn press_e(&mut self) {
        match self.tabs.index {
            0 => {}
            1 => {}
            2 => {}
            3 => {
                if let Some(id) = &self.services.state_id {
                    let _ = self.execute_command(vec!["execute".to_string(), id.to_string()]).await;
                } 
                else {
                    self.logs.push("No service state ID available to execute.".to_string());
                }
            }
            _ => {}
        }
    }

    pub async fn refresh(&mut self) {
        self.peers.refresh(get_peers().unwrap_or_default());
        self.clients.refresh(get_clients().unwrap_or_default());
        self.instances.refresh(get_instances().unwrap_or_default());
        self.services.refresh(get_services().unwrap_or_default());
        self.envs.refresh(get_envs().unwrap_or_default());
        self.tunnels.refresh(get_tunnels().unwrap_or_default());
        self.ram_usage.push(get_ram_usage(&mut self.sys));
        self.cpu_usage.push(get_cpu_usage(&mut self.sys));
    }
}
