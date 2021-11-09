
from rgb_yuv import rgb_to_yuv, yuv_to_rgb
from run_length_alg import encode_message, decode_message
import cv2
from dct import dct_idct


if __name__ == '__main__':

    #exercise 1
    print("EXERCISE 1")
    print("RGB to YUV", rgb_to_yuv(3, 20, 30))
    print("YUV to RGB", yuv_to_rgb(29.791, 134.906, 119.827))

    #exercise 4
    print("EXERCISE 4")
    # the original string
    our_message = "HolaBoneeeees"
    # pass in the original string
    encoded_message = encode_message(our_message)
    # pass in the decoded string
    decoded_message = decode_message(encoded_message)
    print("Original string: [" + our_message + "]")
    print("Encoded string: [" + encoded_message + "]")
    print("Decoded string: [" + decoded_message + "]")

    #exercise 5
    print("EXERCISE 5")
    img = cv2.imread('Lenna.png', 0)
    dct_idct(img)




