import argparse
from avm.fullimg_inference import fullimg_run
from avm.subimg_inference import subimg_run




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    args.exp_id = 0
    args.gpu_used = '106'
    args.confid_thresh = 0.5
    args.pth_type = 'best'
    args.save_plotted_img = True
    args.img_show = True
    args.date = '20220424'
    args.video_id = 'output'
    args.avm_dir = r'E:\Desktop\gpsd\general_parking_slot_detection\mydata'
    args.video_type = 'mp4'
    args.new_folder = True
    print(args)
    #fullimg_run(args)
    subimg_run(args)