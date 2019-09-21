def get_dp_index(*dps):
    new_dps = dps[0]

    for dp in dps[1:]:
        new_dps.extend(reset_index(len(new_dps), dp))

    return ','.join([str(i) for i in new_dps])


def reset_index(nxt_idx=0, dp_index=[]):
    next_index = nxt_idx
    new_indices = []
    current_indices = [0]

    for _ in dp_index:
        current_indices.append(next_index)
        next_index += 1

    for i, dp in enumerate(dp_index):
        if dp != 'None':
            idx = 0 if dp == '0' else current_indices[int(dp)]
            new_indices.append(idx)

    return new_indices


out1 = get_dp_index(['None', '0', '1', '2'], ['None', '0', '1', '2', '5', '1'],
                    ['None', '0', '1'])

out2 = get_dp_index(['None', '0', '1', '2'], ['None', '0', '1', '2', '5', '1'],
                    ['None', '0', '1'])

out3 = get_dp_index(['None', '3', '3', '0'], ['None', '2', '0', '2'])

print(out1)
print(out2)
print(out3)
'''
None,0,1,2,0,4,5,8,4,0,9
None,0,1,2,0,4,5,8,4,0,9
None,3,3,0,5,0,5
'''