This repository is intended to collect my bachelor's and master's physics notes in a _wiki-like_ structure. 

The notes are written in Markdown and intended to be read in **Obsidian**, which supports the `[[wikilinks]]` and mathematical notation used throughout the repository. To browse them with working internal links, download or clone the repository and open its folder as an Obsidian vault. 

## Organization

### Topics and individual notes

Notes are stored as `.md` files in folders representing topics. Each topic folder contains an **overview note with the same name as the folder**. This note introduces the topic and links to all notes and subtopics directly within that folder.

Topics may contain individual notes, nested subtopics, or both. Each subtopic follows the same structure: a folder containing its own overview note and any related notes or further subtopics.

For example, part of the structure for _Quantum mechanics_ could look like this:

- `Quantum mechanics/`
    - `Quantum mechanics.md` — overview of the topic, with links to its subtopics.
    - `Approximation methods/`
        - `Approximation methods.md` — overview, with links to the methods covered.
        - `Variational method/`
            - `Variational method.md` — explanation of the method, with links to examples.
            - `Helium atom — variational method.md` — application to the helium atom.
        - `Time-independent perturbation theory/`
            - `Time-independent perturbation theory.md` — explanation of the method, with links to examples.
            - `Helium atom — perturbation theory.md` — application to the helium atom.


In general, individual notes should approximately remain below 2,000 words. If a note becomes too long, it should be reorganized as a topic: retain an overview note and split the detailed content into separate notes within that topic's folder.

### Links

Each note should begin with a link identifying its parent topic:

```
Parent: [[Name of the parent topic note]]
```

For example, a note applying the variational method to the helium atom would begin with:

```
Parent: [[Variational method]]
```

All the topics or notes mentioned in a note should also be linked when appropriate.

### Case studies

The same physical system, model, or device may appear in several topics. For example, in these notes the helium atom is studied using both the variational method and perturbation theory.

In these cases, a general introductory note should be placed in `Physical systems/`. This note should describe the system and link to its specific treatments, leaving detailed derivations to those individual notes.

Each specific treatment should link back to the general case-study note. Its title should identify the approach used, so that notes about the same system remain easy to distinguish. For example:

- `Helium atom.md` — general introduction in `Case studies/`.
- `Helium atom — variational method.md` — treatment within the variational-method topic.
- `Helium atom — perturbation theory.md` — treatment within the perturbation-theory topic.

### Mathematical results

Notes on mathematical theorems and results should be placed in `Maths/`, unless they are specific to a particular physical application. Physics notes should link to these mathematical notes when using their results, rather than repeat the same explanation in several places.

### Images and graphs

Store images, graphs, and other supporting files in an `Asset/` folder inside the relevant major topic folder. Notes in its subtopics should use that same asset folder.

## Writing conventions

- **Titles:** use clear, descriptive titles. Avoid an initial article unless it is necessary: use _Helium atom_, for example, rather than _The helium atom_.
- **Mathematics:** use `$...$` for inline mathematics and `$$...$$` for display equations. Treat equations as parts of sentences, including appropriate commas and full stops. Avoid blank lines between display equations and the surrounding prose.
- **References:** end every note with a `References` heading listing the sources used. If language models or other AI tools contributed to the note, state this explicitly.