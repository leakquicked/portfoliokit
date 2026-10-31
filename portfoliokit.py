import argparse
from pathlib import Path
def build(root):
 rows=["# Project Inventory",""]
 for p in sorted(Path(root).iterdir()):
  if p.is_dir():rows.append(f"- **{p.name}/** — directory")
  elif p.is_file():rows.append(f"- **{p.name}** — {p.stat().st_size} bytes")
 return "\n".join(rows)+"\n"
def main():
 a=argparse.ArgumentParser();a.add_argument("directory");a.add_argument("--output",default="PROJECTS.md");x=a.parse_args()
 Path(x.output).write_text(build(x.directory),encoding="utf-8");print("Wrote",x.output)
if __name__=="__main__":main()
