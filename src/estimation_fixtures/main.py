
from .cli import EstimationArgParser, EstimationFixturesCLI

def main():
    print("X")
    parser = EstimationArgParser()
    args = parser.parse_args()
    data = { x: getattr(args, x) for x in dir(args) if not(x.startswith("__") or x.startswith("_"))}
    print(data)
    ef_cli = EstimationFixturesCLI(**data)
    ef_cli.issue_command()
    pass




if __name__ == "__main__":
    main()
    pass
