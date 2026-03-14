def main(port: int = 8501):
    """Entry point for CLI dev command."""
    from sample.api.main import start

    print(f"🚀 Starting Sample app on port {port}...\n")
    start(port)


if __name__ == "__main__":
    main(port=8501)
