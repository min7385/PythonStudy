# pip install split-folders
import splitfolders

# test/validation/train 폴더로 데이터 분할
splitfolders.ratio('./images', output='split_whale', seed=1,  ratio=(.8, .0, .2))