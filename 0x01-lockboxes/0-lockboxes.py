#!/usr/bin/python3
'''A module for working out lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (index) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    opened_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in opened_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            opened_boxes.add(boxIdx)
    return n == len(opened_boxes)
