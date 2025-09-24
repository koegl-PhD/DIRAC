from pathlib import Path
from typing import List, Tuple, Union


def collect_fixed_moving_paths(root: Union[str, Path]) -> List[Tuple[Path, Path]]:
    """Return (fixed, moving) .nii.gz path pairs from all *preprocessed* trees below root."""
    root = Path(root)
    fixed = []
    moving = []
    for pre in root.rglob("preprocessed"):
        a_dirs = sorted([p for p in pre.iterdir() if p.is_dir()
                        and p.name.startswith("a_")])
        b_dirs = sorted([p for p in pre.iterdir() if p.is_dir()
                        and p.name.startswith("b_")])

        a_files = []
        for d in a_dirs:
            a = sorted([f for f in d.glob("*.nii.gz") if f.is_file()
                       and not f.name.endswith("_seg.nii.gz")])
            if a:
                a_files.append(a[0])

        b_files = []
        for d in b_dirs:
            b = sorted([f for f in d.glob("*.nii.gz") if f.is_file()
                       and not f.name.endswith("_seg.nii.gz")])
            if b:
                b_files.append(b[0])

        if not a_files or not b_files:
            continue

        fixed.append(b_files[0])
        moving.append(a_files[0])

    return fixed, moving


if __name__ == "__main__":
    fixed, moving = collect_fixed_moving_paths(
        Path("/home/koeglf/data/for_dirac/train"))

    for f, m in zip(fixed, moving):
        print(f"fixed: {f}\nmoving: {m}\n\n\n")

    x = 0
