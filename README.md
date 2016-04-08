# distance-precomputation
Builds a dictionary of distances between postal codes from REST API

## Summary
Given an input file of postal codes (one per line), this script calls a REST endpoint on the web to get the distance between those two points. The points and the distance between them in both directions is stored for later use.

The script uses the results file as a cache and if interrupted will resume from where it was stopped.

On completion, the precomputed values are stored in a local file for rapid access during analysis.
