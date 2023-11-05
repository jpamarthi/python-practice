def find_pyramid_height(blocks):
    """Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

    Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

    Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

    Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

    Test your code using the data we've provided.

    Sample input: 6

    Expected output: The height of the pyramid: 3
    Sample input: 20

    Expected output: The height of the pyramid: 5

    Sample input: 1000

    Expected output: The height of the pyramid: 44

    Sample input: 2

    Expected output: The height of the pyramid: 1
    """
    # 1. Assign the value of height to 0
    height = 0

    # 2. Loop condition to check weather the block is not equal to zero and blocks >= height + 1
    while (blocks != 0) and (blocks >= height + 1):
        # 2a. increment height
        height += 1

        # 2b. sub blocks - height
        blocks -= height

    # print("The height of the pyramid:", height)
    return height

