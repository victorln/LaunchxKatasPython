

#Tracebacks
# def main():
#     open("/path/to/mars.jpg")

# if __name__ == '__main__':
#     main()

#Controlando excepciones con Try y Except
try:
    open('config.txt')
except:
    print("Couldn't find the config.txt file")
