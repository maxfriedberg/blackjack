import random
from charts import hard_chart
from charts import soft_chart
from charts import pairs_chart
from charts import sort_hand
from charts import make_move

test_hands1 = [ [ 'A', '4' ], [ '3', '10' ], [ '3', '4', '5' ] ]
test_hands2 = [ [ 'A', 'A' ] ]
test_hands3 = [ [ '7', '8' ], [ '7', '7', '2' ] ]

test_hands4 = [ [ 'A', '4' ], [ '3', '10' ], [ '3', '4', '5' ] ]
test_hands5 = [ [ 'A', 'A' ] ]
test_hands6 = [ [ '7', '8' ], [ '7', '7', '2' ] ]


for hand in test_hands1:
    for upcard in range(2, 10):
        move = make_move(hand, len(test_hands1), str(upcard))
        print(move)