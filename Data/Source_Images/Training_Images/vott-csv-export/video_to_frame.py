import cv2

# Opens the Video file
cap= cv2.VideoCapture('/Users/wdavis4/Desktop/LA/bike1_output.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if len(str(i)) == 1:
        cv2.imwrite('/Users/wdavis4/Desktop/LA/frame000000'+str(i)+'.jpg',frame)
        i+=1
    if len(str(i)) == 2:
        cv2.imwrite('/Users/wdavis4/Desktop/LA/frame00000'+str(i)+'.jpg',frame)
        i+=1
    if len(str(i)) == 3:
        cv2.imwrite('/Users/wdavis4/Desktop/LA/frame0000'+str(i)+'.jpg',frame)
        i+=1
    if len(str(i)) == 4:
        cv2.imwrite('/Users/wdavis4/Desktop/LA/frame000'+str(i)+'.jpg',frame)
        i+=1
    if len(str(i)) == 5:
        cv2.imwrite('/Users/wdavis4/Desktop/LA/frame00'+str(i)+'.jpg',frame)
        i+=1
    if len(str(i)) == 6:
        cv2.imwrite('/Users/wdavis4/Desktop/LA/frame0'+str(i)+'.jpg',frame)
        i+=1
    if i % 1000 == 0:
        progress = str(i/19.5/10) + '%'
        print(progress)
cap.release()
cv2.destroyAllWindows()