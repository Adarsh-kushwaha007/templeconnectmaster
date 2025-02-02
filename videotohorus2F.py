import os
import shutil
import cv2

sInputFileName=''
sDataBaseDir=''
if os.path.exist(sDataBaseDir):
    shutil.rmtree(sDataBaseDir)

if not os.path.exist(sDataBaseDir):
    os.makedirs(sDataBaseDir)
print('=================================================')
print('Start Movie to Frames')
print('=================================================')
vidcap=cv2.VideoCapture(sInputFileName)
success,image=vidcap.read()
count=0
while success:
    success,image=vidcap.read()
    sFrame=sDataBaseDir+str('/dog-frame-'+str(format(count,'04d'))+'.jpg')
    print('Extracted: ', sFrame)
    cv2.imwrite(sFrame, image)
    if os.path.getsize(sFrame) == 0:
        count+=-1
        os.remove(sFrame)
    print('Removed:',sFrame)
    if cv2.waitKey(10)==27:
        break
    count +=1
print('=====================================================')
print('Generated : ', count, ' Frames')
print('=====================================================')
print('Movie to Frames HORUS - Done')

print('=====================================================')
