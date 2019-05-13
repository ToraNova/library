
#takes URL of image and Path for the image as parameter

function download_image1(){
    fp = $(fopen $1 w+)              #open file handle

    ch = $(curl_init $1)
    #curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); #enable if you want
    curl_setopt $ch CURLOPT_FILE $fp          #output to file
    curl_setopt $ch CURLOPT_FOLLOWLOCATION 1
    curl_setopt $ch CURLOPT_TIMEOUT 1000      #some large value to allow curl to run for a long time
    curl_setopt $ch CURLOPT_USERAGENT 'Mozilla/5.0'
    #curl_setopt($ch, CURLOPT_VERBOSE, true);   #Enable this line to see debug prints
    curl_exec $ch

    curl_close $ch                              #closing curl handle
    fclose $fp                                  #closing file handle
}

download_image1 "192.168.0.103/htmlbot/cam_get.php" "img1.jpg"
