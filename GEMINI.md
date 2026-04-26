# Project: SEL Lecture Slides

This repository contains educational lecture slides for courses at the Department of Electrical and Computer Engineering (SEL) of the Sao Carlos School of Engineering (EESC-USP). The slides are primarily focused on **SEL0383 - Sinais e Sistemas** (Signals and Systems).

## Project Overview

The slides are built using [Reveal.js](https://revealjs.com/), a framework for creating HTML presentations. It utilizes KaTeX for mathematical notation and Vis-graph3d for 3D visualizations.

### Main Technologies
- **Reveal.js**: Presentation framework.
- **KaTeX**: LaTeX math rendering.
- **Vis-graph3d**: 3D data visualization.
- **HTML/CSS/JS**: Core web technologies.

## Directory Structure

- `2024/`, `2025/`: Academic years containing course-specific directories.
  - `SEL0383/`: Signals and Systems course slides.
  - `SEL0604/`: Other course materials.
- `images/`: A comprehensive library of technical illustrations, block diagrams, and mathematical plots used across all presentations.
- `reveal.js/`: The Reveal.js core library and plugins.
- `init.js`: Shared initialization script for Reveal.js. It configures plugins (Markdown, Highlight, Notes, KaTeX) and presentation settings (width, height, transition).
- `style.css`: Global custom styles for consistent slide appearance.
- `plot3d.html`: A template or demo for integrating 3D line plots using `vis-graph3d`.

## Usage and Development

### Viewing Slides
To view the slides, open any `aulaX.html` file (e.g., `2025/SEL0383/aula1.html`) in a modern web browser.

### Creating New Slides
1.  **Template**: Use an existing `aula.html` as a template.
2.  **Asset Paths**: Ensure relative paths to `reveal.js/`, `images/`, `style.css`, and `init.js` are correct (usually `../../` from within a subfolder).
3.  **Math**: Use `$` for inline math and `$$` for block math, as configured in `init.js`.
4.  **Images**: Reference images from the central `images/` directory to maintain consistency.

### Customization
- **Initialization**: Modify `init.js` to change global presentation behavior (e.g., transitions, slide dimensions).
- **Styling**: Update `style.css` for visual adjustments across all lectures.

## Key Conventions
- **Slide Numbers**: Hidden on the first slide using `data-hide-slide-number="true"`.
- **Transitions**: Defaulted to `none` in `init.js` for a clean look, but can be overridden per slide or globally.
- **Math Macros**: Custom LaTeX macros (like `\R`, `\trp`, `\tr`) are defined in `init.js`.
