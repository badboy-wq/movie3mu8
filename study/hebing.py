import os
def heBingTsVideo(download_path, hebing_path):
    all_ts = os.listdir(download_path)  # "合并ts文件"
    # heBingTsVideo(r'D://study/movie/', r'D://study/movie/123456.mp4')

    with open(hebing_path, 'wb+') as f:
        for i in range(len(all_ts)):
            ts_video_path = os.path.join(download_path, all_ts[i])
            f.write(open(ts_video_path, 'rb').read())
    print("合并完成！！")


if __name__ == '__main__':
    heBingTsVideo(r'D://study/movie/bf6c05a9', r'D://study/movie/mp4/777.mp4')