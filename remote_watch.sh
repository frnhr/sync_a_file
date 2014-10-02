#!/usr/bin/env bash
fswatch rebelmouse | xargs -I file ./sync_a_file.py "file"
