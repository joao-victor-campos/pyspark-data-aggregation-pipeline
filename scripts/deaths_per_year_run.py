from spark_pipeline import deaths_per_year_pipeline


def main() -> None:
    """Main."""
    print(">>> Pipeline execution starting...")
    deaths_per_year_pipeline.run()
    print(">>> Pipeline execution finished!!!")


if __name__ == "__main__":
    main()
