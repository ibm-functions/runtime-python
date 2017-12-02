def main(args):
    name = args.get("name", "stranger")
    greeting = "Hello " + name + "!"
    print(greeting)
    return {"greeting": greeting}
tel = {"name": "Carlos"}
if __name__ == "__main__":
    # execute only if run as a script
    main(tel)