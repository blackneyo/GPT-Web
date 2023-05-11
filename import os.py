import os

image_dir = "C:\Users\4lab\Desktop\dat\images"
label_dir = "C:\Users\4lab\Desktop\dat\labels"

# 이미지 파일 이름 목록 가져오기
image_files = os.listdir(image_dir)
image_filenames = [os.path.splitext(filename)[0] for filename in image_files]

# 라벨 파일 이름 목록 가져오기
label_files = os.listdir(label_dir)

# 라벨 파일 중 이미지 파일 이름과 일치하지 않는 것들 삭제하기
for label_file in label_files:
    label_filename, ext = os.path.splitext(label_file)
    if ext == ".txt" and label_filename not in image_filenames:
        os.remove(os.path.join(label_dir, label_file))

print("삭제 완료!")