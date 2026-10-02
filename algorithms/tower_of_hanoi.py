def hanoi_solver(number_of_disks):
    # The three real rods: fixed positions, never renamed
    rod_1 = list(range(number_of_disks, 0, -1))
    rod_2 = []
    rod_3 = []

    def get_state():
        # Always prints rod_1, rod_2, rod_3 in this order
        return f"{rod_1} {rod_2} {rod_3}"

    moves = [get_state()]  # starting arrangement

    def solve(disks, from_rod, to_rod, spare_rod):
        # Roles change with each call; positions never do
        if disks == 0:
            return
        solve(disks - 1, from_rod, spare_rod, to_rod)
        to_rod.append(from_rod.pop())
        moves.append(get_state())
        solve(disks - 1, spare_rod, to_rod, from_rod)

    solve(number_of_disks, rod_1, rod_3, rod_2)
    return "\n".join(moves)

print(hanoi_solver(3))