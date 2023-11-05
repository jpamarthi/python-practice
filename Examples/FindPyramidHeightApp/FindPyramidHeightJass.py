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
    # height = 0
    # while a > 0:
    #     height += 1
    #     a -= height
    # return height
    # 2. Assign the value of height to 0

    height = 0

    # 3. Assign the value of num_of_blocks to 0
    num_of_blocks = 0

    # 4. Loop condition to check weather the block is not equal to zero and blocks >= height + 1
    while (blocks != 0) and (blocks >= height + 1):
        # 4a. increment height
        height += 1

        # 4b. add num_of_blocks + height
        num_of_blocks += height

        # 4c. sub blocks - height
        blocks -= height

    # print("The height of the pyramid:", height)
    return height

