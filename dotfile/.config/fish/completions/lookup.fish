# Define a completion function for lookup
function __fish_lookup_complete
    # Get the current token (the word being completed)
    set -l cur (commandline -ct)

    # Call lookup --complete with the current token + '*'
    set -l completions (lookup --complete -- "$cur*")

    # Output each possible completion on a new line
    for completion in $completions
        echo $completion
    end
end

# Register the completion function for lookup
complete -c lookup -f -a '(__fish_lookup_complete)'

