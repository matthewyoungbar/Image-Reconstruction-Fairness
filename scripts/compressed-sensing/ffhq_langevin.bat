python src/compressed_sensing.py --checkpoint-path ./checkpoints/ncsnv2_ffhq/checkpoint_80000.pth --net ncsnv2 --dataset ffhq-69000 --num-input-images 1 --batch-size 1 --ncsnv2-configs-file ./ncsnv2/configs/ffhq.yml --measurement-type circulant --noise-std 4.0 --num-measurements 5000 --model-type langevin --print-stats --checkpoint-iter 1 --cuda --mloss-weight 0.1 --learning-rate 9e-6 --sigma-init 348 --sigma-final 0.01 --L 2311 --T 3

python src/compressed_sensing.py --checkpoint-path ./checkpoints/ncsnv2_ffhq/checkpoint_80000.pth --net ncsnv2 --dataset ffhq-69000 --num-input-images 1 --batch-size 1 --ncsnv2-configs-file ./ncsnv2/configs/ffhq.yml --measurement-type circulant --noise-std 4.0 --num-measurements 10000 --model-type langevin --print-stats --checkpoint-iter 1 --cuda --mloss-weight 0.1 --learning-rate 9e-6 --sigma-init 348 --sigma-final 0.01 --L 2311 --T 3

python src/compressed_sensing.py --checkpoint-path ./checkpoints/ncsnv2_ffhq/checkpoint_80000.pth --net ncsnv2 --dataset ffhq-69000 --num-input-images 1 --batch-size 1 --ncsnv2-configs-file ./ncsnv2/configs/ffhq.yml --measurement-type circulant --noise-std 4.0 --num-measurements 15000 --model-type langevin --print-stats --checkpoint-iter 1 --cuda --mloss-weight 0.1 --learning-rate 9e-6 --sigma-init 348 --sigma-final 0.01 --L 2311 --T 3

python src/compressed_sensing.py --checkpoint-path ./checkpoints/ncsnv2_ffhq/checkpoint_80000.pth --net ncsnv2 --dataset ffhq-69000 --num-input-images 1 --batch-size 1 --ncsnv2-configs-file ./ncsnv2/configs/ffhq.yml --measurement-type circulant --noise-std 4.0 --num-measurements 20000 --model-type langevin --print-stats --checkpoint-iter 1 --cuda --mloss-weight 0.1 --learning-rate 9e-6 --sigma-init 348 --sigma-final 0.01 --L 2311 --T 3

python src/compressed_sensing.py --checkpoint-path ./checkpoints/ncsnv2_ffhq/checkpoint_80000.pth --net ncsnv2 --dataset ffhq-69000 --num-input-images 1 --batch-size 1 --ncsnv2-configs-file ./ncsnv2/configs/ffhq.yml --measurement-type circulant --noise-std 4.0 --num-measurements 30000 --model-type langevin --print-stats --checkpoint-iter 1 --cuda --mloss-weight 0.09 --learning-rate 9e-7 --sigma-init 348 --sigma-final 0.001 --L 2311 --T 3

python src/compressed_sensing.py --checkpoint-path ./checkpoints/ncsnv2_ffhq/checkpoint_80000.pth --net ncsnv2 --dataset ffhq-69000 --num-input-images 1 --batch-size 1 --ncsnv2-configs-file ./ncsnv2/configs/ffhq.yml --measurement-type circulant --noise-std 4.0 --num-measurements 40000 --model-type langevin --print-stats --checkpoint-iter 1 --cuda --mloss-weight 0.1 --learning-rate 9e-7 --sigma-init 348 --sigma-final 0.001 --L 2311 --T 3

python src/compressed_sensing.py --checkpoint-path ./checkpoints/ncsnv2_ffhq/checkpoint_80000.pth --net ncsnv2 --dataset ffhq-69000 --num-input-images 1 --batch-size 1 --ncsnv2-configs-file ./ncsnv2/configs/ffhq.yml --measurement-type circulant --noise-std 4.0 --num-measurements 50000 --model-type langevin --print-stats --checkpoint-iter 1 --cuda --mloss-weight 0.1 --learning-rate 9e-7 --sigma-init 348 --sigma-final 0.001 --L 2311 --T 3

python src/compressed_sensing.py --checkpoint-path ./checkpoints/ncsnv2_ffhq/checkpoint_80000.pth --net ncsnv2 --dataset ffhq-69000 --num-input-images 1 --batch-size 1 --ncsnv2-configs-file ./ncsnv2/configs/ffhq.yml --measurement-type circulant --noise-std 4.0 --num-measurements 75000 --model-type langevin --print-stats --checkpoint-iter 1 --cuda --mloss-weight 0.1 --learning-rate 9e-7 --sigma-init 348 --sigma-final 0.001 --L 2311 --T 3 
