from server import init_api


HOST = "localhost"

def main():
    app = init_api()
    app.run(host="localhost", port=8080, debug=False)


if __name__ == "__main__":
    main()