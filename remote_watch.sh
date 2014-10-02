#!/usr/bin/env bash
fswatch local | xargs -I file ./sync_a_file.py "file"
