def get_dp_index(*dps):
    new_dps = dps[0]

    for dp in dps[1:]:
        new_dps.extend(reset_index(len(new_dps), dp))

    return ','.join([str(i) for i in new_dps])


def reset_index(nxt_idx=0, dp_index=[]):
    next_index = nxt_idx
    new_indices = []
    current_indices = [0]

    for i in range(1, len(dp_index)):
        current_indices.append(next_index)
        next_index += 1

    for i, dp in enumerate(dp_index):
        if dp != 'None':
            new_indices.extend(
                [0 if dp == '0' else current_indices[int(dp_index[i])]])
    return new_indices


# print(
#     get_dp_index(['None', '0', '1', '2'], ['None', '0', '1', '2', '5', '1'],
#                  ['None', '0', '1']))

print(
    get_dp_index(['None', '0', '1', '2'], ['None', '0', '1', '2'],
                 ['None', '0', '4', '5'], ['None', '0', '1']))