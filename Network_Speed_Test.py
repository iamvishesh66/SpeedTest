import time
import speedtest
print("This is cmd line software which tests you network speed\n")
try:
    def main():
        convert_var = 1024 * 1024
        print("Loading")
        s = speedtest.Speedtest()
        print("Checking upload speed...")
        upload = s.upload()
        print("Checking Download Speed...")
        download = s.download()
        print("I Hope your internet was fast")
        print("Download Speed\t{0}MBPS\nUpload Speed\t{1}MBPS".format(round(download / convert_var), round(upload / convert_var)))
        time.sleep(15)
        exit()
    main()
except:
    print("\nERROR!!!\nNO Active Network Connection")
    for i in range(3):
        print("\nPlease connect to a network to test speed///...///...")
        time.sleep(15)
        try:
            main()
        except:
            print("Try AGAIN, connecting to a network to test speed")
    
