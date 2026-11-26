# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):

    # Outline (write your plan here first):
    #   Make a smaller function that does the multiplication
    #   then make a list of task calls per number, then use
    #   asyncio to run all of them

    async def task(n):
        await asyncio.sleep(0.1)
        return n * 2
    
    tasks = [ task(n) for n in numbers ]

    return await asyncio.gather(*tasks)


async def fastest(jobs):
    # Outline:
    #   Using the previous system
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)

    async def task(label: str, delay: float):
        await asyncio.sleep(delay)
        return label
    
    # Create tasks for the coroutines
    tasks = [
        asyncio.create_task(
            task(job[0] ,job[1])
        )
        for job in jobs
    ]

    ordered_results = []

    # Iterate over the completed tasks as they finish
    for future in asyncio.as_completed(tasks):
        result = await future
        ordered_results.append(result)

    if len(ordered_results) == 0: return
    return ordered_results[0]


def echo_once(host, port, message):
    # Outline:
    #   1. Create a socket, connect to the server
    #   2. Send the encoded message
    #   3. Wait for and read the response
    #   4. Return the decoded response message

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        client.sendall( message.encode() )

        back = client.recv(1024)

        return back.decode()

    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    pass


def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()
