import re

input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day5/erika-input.txt")

with input as f:
    seed_text = f.read()

def seed_1(text):
    seeds = []
    seed_maps = []

    for line in text.split("\n"):
        if len(line) != 0:
            if re.match("^seeds:.+", line):
                seeds = re.findall(r"\d+", line)
            elif re.match(".*map:", line):
                seed_maps.append([])
            else:
                decoded_map = re.match(r"(\d+) (\d+) (\d+)", line)
                if decoded_map:
                    seed_maps[-1].append(
                        {
                            "destination": int(decoded_map.group(1)),
                            "source": int(decoded_map.group(2)),
                            "range": int(decoded_map.group(3)),
                        }
                    )
    results = []
    for seed in seeds:
        current_type = int(seed)
        for seed_map in seed_maps:
            for single_seed_map in seed_map:
                if current_type - single_seed_map["source"] >= 0 and current_type - single_seed_map["source"] < single_seed_map["range"]:
                    current_type = current_type - single_seed_map["source"] + single_seed_map["destination"]
                    break

        results.append(current_type)
    
    return min(results)

def seed_2(text):
    seeds = []
    seed_maps = []

    for line in text.split("\n"):
        if len(line) != 0:
            if re.match("^seeds:.+", line):
                for seed_pair in re.findall(r"(\d+) (\d+)", line):
                    seeds.append({
                        "start": int(seed_pair[0]),
                        "end": int(seed_pair[0]) + int(seed_pair[1]) -1
                    })
            elif re.match(".*map:", line):
                seed_maps.append([])
            else:
                decoded_map = re.match(r"(\d+) (\d+) (\d+)", line)
                if decoded_map:
                    seed_maps[-1].append(
                        {
                            "difference": int(decoded_map.group(2)) - int(decoded_map.group(1)),
                            "source_start": int(decoded_map.group(2)),
                            "source_end": int(decoded_map.group(2)) + int(decoded_map.group(3)) -1,
                        }
                    )
    def sortBySource(map):
        return map["source_start"]
    
    for i, seed_map in enumerate(seed_maps):
        seed_map.sort(key=sortBySource)

    these_ranges = seeds

    for seed_map in seed_maps:
        next_ranges = []
        for seed in these_ranges:
            current_seed_start = seed["start"]
            for single_seed_map in seed_map:
                possible_start = max(single_seed_map["source_start"], current_seed_start)

                if possible_start > seed["end"]:
                    break

                possible_end = min(single_seed_map["source_end"], seed["end"])

                if possible_end >= possible_start:
                    if current_seed_start < possible_start:
                        next_ranges.append({
                            "start": current_seed_start,
                            "end": possible_start - 1
                        })
                    next_ranges.append({
                        "start": possible_start - single_seed_map["difference"],
                        "end": possible_end - single_seed_map["difference"]
                    })
                    current_seed_start = possible_end + 1

            if current_seed_start < seed["end"]:
                next_ranges.append({
                    "start": current_seed_start,
                    "end": seed["end"]
                })

        these_ranges = next_ranges.copy()
    
    def sortByStart(seed):
        return seed["start"]
            
    next_ranges.sort(key=sortByStart)
    
    return next_ranges[0]["start"]

val = seed_2(seed_text)
print(val)