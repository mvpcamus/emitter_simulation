#!/bin/bash
WIDTH=50
LAYER=4
RADIUS=1.0
EFFECT_D=20.0
STEP_X=6.1
STEP_Z=6.5
ACT_RATE=95
NUM_Q=400

python3 count3d.py $WIDTH $LAYER $RADIUS $EFFECT_D $STEP_X $STEP_Z $ACT_RATE $NUM_Q | tee "$ACT_RATE"%_"$STEP_Z"_"$WIDTH"x"$WIDTH"x"$LAYER"_"$EFFECT_D"_"$NUM_Q".txt
