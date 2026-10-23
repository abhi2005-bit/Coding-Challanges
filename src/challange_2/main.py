import argparse
from challange_2.validator import validator
def main():
    parser=argparse.ArgumentParser(description="this is a json parser ")
    parser.add_argument("filename",help="json file to check")

    args=parser.parse_args()

    print(args.filename)
    with open(args.filename,"r")as file:
        data=file.read()
    print(data)
    print(validator(args.filename))

if __name__=="__main__":
    main()