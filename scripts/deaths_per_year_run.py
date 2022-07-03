from spark_pipeline.deaths_per_year import extract, load, transform


def main() -> None:
    """Main."""
    load(transform(extract()))
    print(">>> Pipeline execution finished!!!")


if __name__ == "__main__":
    main()
