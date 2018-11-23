import re


def get_half(seq):
    ssr_obj = re.search(r'([ATCG]+)\1', seq)
    if ssr_obj:
        return ssr_obj.group(1)
    else:
        return None


def check_tail(block, sequence, terminal):
    block_len = len(block)
    potential_tail = sequence[terminal: (terminal + block_len)]
    if potential_tail == block:
        return 1, block_len
    else:
        return 0, 0


def scan_kmer(kmer):
    """ kmer is the seed to be considered each time.
        It's a partial sequence or a fasta object, and
        it's not necessary to be the same length as
        given in multiple line fasta file.
    """
    ssr_obj = re.search(r'([ATCG]+)\1', kmer)
    if ssr_obj and len(ssr_obj.group()) >= 6:
        half = kmer
        start_pos = ssr_obj.start(0)
        end_pos = ssr_obj.end(0)

        time = 2
        while half:
            unit = half
            half = get_half(half)
            if half:
                time = 2*time
            else:
                return unit, start_pos, end_pos, time
    else:
        return None
    

def calibrate_kmer(k):
    """
    correct the times of repeated unit
    by adding the possible missing single one at the end.
    """

    k_result = scan_kmer(k)
    if k_result:
        repeat, pos = check_tail(k_result[0], k, k_result[2] + 1)
        k_result[3] += repeat
        k_result[2] += pos
    return k_result
