from cpp_demangle import demangle
import requests
def demangleImpl_():
    try:
        i = input("Demangle: ")
        print(demangle(i))
        inputget()
    except:
        inputget()
def asmImpl_():
    try:
        i = input("Convert: ")
        url = requests.post('https://armconverter.com/api/convert', json = {"asm":i,"offset":"","arch":"arm64"}).json()
        print(f"{str(url['hex']['arm64'][1])}")
        inputget()
    except:
        inputget()
def callAsmImpl_():
    try:
        pc, dest = input("From, To: ").split()
        pc = (int(pc, 16))
        dest = (int(dest, 16))
        res = str(hex(dest - pc))
        url = requests.post('https://armconverter.com/api/convert', json = {"asm":f"BL #{res}","offset":"","arch":"arm64"}).json()
        print(f"{str(url['hex']['arm64'][1])}")
        inputget()
    except:
        inputget()
def inputget():
    try:
        print()
        print("Useless Patch/C++ tools")
        print("1 - Cpp Demangler")
        print("2 - Convert Arm to Hex")
        print("3 - Convert call (from, to)")
        print()
        a = input()
        print()
        if a == '1':
            demangleImpl_()
        elif a == '2':
            asmImpl_()
        elif a == '3':
            callAsmImpl_()
        else:
            print("bruh u dumb read the instructions")
            inputget()
    except:
        inputget()
inputget()