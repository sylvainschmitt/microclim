# microclim
Oct 9, 2025

**microclim** is a project that aims to exploit the micrometeorological
loggers installed by the ALT project in 2023 to improve our
understanding of the horizontal, vertical and temporal variations in the
microclimate of tropical forests.

> How do canopy openness, vegetation density and micropography (water
> and soil texture) affect topsoil, surface and aboveground air
> temperature, and topsoil moisture?

The objective are:

- Data gathering: microclimate ((HOBO), macroclimate (ERA5-Land &
  MeteoFrance), eddy flux (Guyaflux), vegetation structure (mulitple
  lidars, phenobs?), microtopography (lidar), and pedology
- Climate data temporal decomposition: using Fourrier Fast
  Transformation
  (e.g. <https://www.fortran.cnrs.fr/wp-content/uploads/2025/07/fortran-hingant.pdf>)
- Forest and microclimate offset computation
- Statistical exploration of horizontal and temporal drivers
- Simplified mechanistic modelling

## Project

**microclim** includes all codes to access the data (in `data/`) &
analyse the data (`files.qmd`) with associated [documentation and
figures](https://sylvainschmitt.github.io/microclim/). Intermediary
files and outputs can be accessed in `outputs/`. The project takes
advantage of `renv` to manage the R environment for enhanced
reproducibility.

> To be reviewed later splitting raw and derived data.

## Contribution

You can contribute to the project by forking the repository on github
and cloning the fork to your machine using several options, including
GitHub desktop GUI. Access to the data is limited and can be requested
by emailing people from the core group (see below). Further informations
on contribution are detailed in the online document:
<https://sylvainschmitt.github.io/microclim/98_contributing.html>.

## Help

Please preferentially create an issue on GitHub for any questions, bugs
or help needed regarding **microclim**:
<a href="https://github.com/Bsylvainschmitt/microclim/issues"
class="uri">https://github.com/sylvainschmitt/microclim/issues</a> . You
may however reach us by mail with people from the core group (see
below).

## Core group

- Sylvain Schmitt CIRAD

- Erwan Hingant University of Picardie Jules Verne

- Jonathan Lenoir CNRS

- Vincyane Badouard ADEME

- Géraldine Derroire CIRAD

- Grégoire Vincent IRD

- Éric Marcon APT
