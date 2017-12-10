from app import app

if __name__ == '__main__':
    print(" * Starting SmartVet main server.")
    app.run(host='0.0.0.0', port=9292, debug=True)
