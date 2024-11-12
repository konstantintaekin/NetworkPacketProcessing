size_buffer, size_cycle = map(int, input().split())
lst_buffer = []
lst_start_operation = []
# answer = []

for i in range(size_cycle):
    time_start, duration = map(int, input().split())
    if lst_buffer == []:
        # answer.append(time_start)
        print(time_start)
        lst_buffer.append([time_start, duration])
        lst_start_operation.append(time_start + duration)
        size_buffer -= 1
    else:
        if time_start >= lst_start_operation[0]:
            lst_buffer.pop(0)
            lst_start_operation.pop(0)
            size_buffer += 1
            if len(lst_buffer) == 0:
                # answer.append(time_start)
                print(time_start)
                lst_buffer.append([time_start, duration])
                lst_start_operation.append(time_start + duration)
                size_buffer -= 1
            elif len(lst_buffer) != 0:
                # answer.append(lst_start_operation[-1])
                print(lst_start_operation[-1])
                lst_buffer.append([time_start, duration])
                lst_start_operation.append(lst_start_operation[-1] + duration)
                size_buffer -= 1
        elif time_start < lst_start_operation[0]:
            if size_buffer != 0:
                # answer.append(lst_start_operation[-1])
                print(lst_start_operation[-1])
                lst_buffer.append([time_start, duration])
                lst_start_operation.append(lst_start_operation[-1] + duration)
                size_buffer -= 1
            elif size_buffer == 0:
                # answer.append(-1)
                print(-1)

# print(*answer)