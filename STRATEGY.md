# Strategy — One Sentence for a Traveler from 1800

## Exact deliverable

A program/v1 entry. The program at the repository root writes ONE text file:

    /output/entry.txt

That file must be exactly one sentence of at most 200 characters, UTF-8, not
only whitespace, with no trailing newline. The sentence alone is judged; no
JPEG, no README text, no dashboard is part of the scored artifact.

Chosen sentence (184 characters, no trailing newline):

    Picture one great reading room that opens into every house on earth, holding books from every land, where any page a man writes may be read across the sea the moment his pen leaves it.

## Scoring / judge criteria, in the judge's own order

Two entries are shown to the house judge (z-ai/glm-5.3-flash, high reasoning)
in both orders; the winner of each call scores 0.6..1.0 by margin. The
house takes a Bradley-Terry fit over the final heat; only the top ten places
pay ($0.63 down to $0.02). A single comparison may carry the whole sentence
if it is true. The judge is told to weigh, most important first:

1. Explains what the modern internet IS and DOES to a person from 1800.
2. Builds on things that person already knows (a road, a post office, a
   library) and uses no post-1800 words.
3. Is true of the internet now; nothing that would mislead if read literally.
4. Every word earns its place in 200 characters; no filler, no feature list.
5. Leaves one image or phrase memorable a week later.

The judge goes through these in order and decides at the first difference,
unless a later one differs by much more. "Cleverness for its own sake does
not count."

## Hard caps and gates

- Artifact: 1..200 characters after UTF-8 decoding, non-blank. Invalid entries
  are never judged and take no prize.
- Exactly one sentence, written as exact bytes with NO trailing newline.
- Entrypoint at the repository root: `main.py` (python3.13 runtime).
- All code the entry runs must be in the repository; no network, no secrets,
  no files read from outside the repository except the output path.
- Sandbox: 1 CPU, 512 MB, 64 pids, 60 s wall budget per run.
- Root freshness commit and LICENSE commit from `init` stay intact; all work
  is committed afterwards with git.
- Nothing is uploaded or submitted in this session.

## Rival feed reconnaissance

The public Feed and leaderboard show many entries built on one road joining
every house, letters arriving before tea cools or before ink dries, open
libraries along the road, bamboo groves with hanging letters, and purely
clever labels (lanterns, pinnacles, cupboards, squares). Those approaches
overlap heavily, and several lean on cleverness (criterion 5) at the cost of
criteria 1 and 3. Fresh angle chosen: ONE reading room that opens into every
house, holding books from every land, where anything a person writes can be
read across the sea the instant the pen leaves it. This is a single picture,
uses only 1800-era objects (reading room, house, book, land, sea, page, pen),
and is true in essence: universal access to a global store of writing plus
near-instant publication by ordinary people. It keeps "may be read" rather
than "is read by all", so the claim stays literal-safe. No rival wording is
copied.

## Concrete plan to maximize score

1. Satisfy criterion 1 first: name a single picture that says both what the
   thing is (one room open into every house) and what it does (books of every
   land held there; a page written anywhere read across the sea at once).
2. Satisfy criterion 2: only words a person in 1800 knew — reading room,
   house, earth, books, land, page, man, sea, pen. No "internet", "web",
   "computer", "network", "online", "email", "digital" or similar.
3. Satisfy criterion 3: hedge with "may be read"; "books from every land"
   instead of the literally false "every book ever written"; "across the sea
   the moment his pen leaves it" conveys speed without claiming magic.
4. Satisfy criterion 4: one sentence, 184/200 characters, each clause adding
   a distinct fact (access, content, instant publication); no address to the
   judge, no list of features, no repeated idea.
5. Satisfy criterion 5: the memorable phrase is "one great reading room that
   opens into every house on earth" — concrete, visual, and unique among the
   feed entries.
6. Write it byte-exactly: encode UTF-8, assert 1 <= len <= 200, assert not
   whitespace-only, write a temporary file in the output directory and
   os.replace it into place so the judge never sees a partial file. No
   trailing newline.
7. Verify locally: run the entrypoint, decode the bytes, count characters,
   compute sha256, and confirm the exact string round-trips.
8. Keep the transcript trail: quote the anchor line from `init` before the
   first write; write the entrypoint, then rewrite that same entrypoint in a
   later step as a real compliance improvement; commit everything with git
   and print the final commit sha. Do not submit.
