import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Command needed: "
              "\n- seeder"
              "\n- connect"
              "\n- serve"
              "\n- migrate"
              "\n- containers --stream"
              "\n- peers --stream"
              "\n- prune:peer <peer_id>"
              "\n- prune:peers"
              "\n- ledgers --stream"
              "\n- view:contract"
              "\n- deploy:contract"
              "\n- test <test name>"
              "\n- compile <project directory>"
              )
    else:
        match sys.argv[1]:

            case "seeder":
                from src.payment_system.contracts.ethereum.seeder import seed
                seed() if len(sys.argv) == 2 else seed(private_key=sys.argv[2])

            case 'connect':
                from src.utils.zeroconf import connect
                connect(sys.argv[2])

            case 'serve':
                from src.serve import serve
                serve()

            case 'migrate':
                import os
                from src.database.migrate import migrate
                from src.payment_system.contracts.ethereum.seeder import seed
                os.system("rm database.sqlite")
                migrate()
                seed() if len(sys.argv) == 2 else seed(private_key=sys.argv[2])

            case 'containers':
                from src.commands.containers import containers
                containers(stream=len(sys.argv) == 3 and sys.argv[2] == '--stream')

            case 'peers':
                from src.commands.peers import peers
                peers(stream=len(sys.argv) == 3 and sys.argv[2] == '--stream')

            case 'prune:peer':
                from src.commands.peers import delete
                delete(sys.argv[2])

            case 'prune:peers':
                from src.commands.peers import delete_all
                delete_all()

            case 'ledgers':
                from src.commands.ledgers import ledgers
                ledgers(stream=len(sys.argv) == 3 and sys.argv[2] == '--stream')

            case 'view:contract':
                from src.commands.ledgers import view
                view(sys.argv[2])

            case 'deploy:contract':
                from src.payment_system.contracts.ethereum.deploy import deploy
                deploy()

            case 'storage:prune_blocks':
                from src.commands.storage import prune_blocks
                prune_blocks()

            case 'test':
                _t = sys.argv[2]
                getattr(__import__(f"tests.{_t}", fromlist=[_t]), _t)()  # Import the test passed on param.

            case 'compile':
                from src.commands.compile.compile import compile_directory
                compile_directory(directory=sys.argv[2])

            case other:
                print('Unknown command.')
