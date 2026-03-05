function H = spectral_entropy(PSD, sf)
    % Inputs:
    % PSD - Power Spectral Density of window
    % sd - scaling factor, needed for normalization of spectral entropy
    %
    %calculates spectral entropy
    %
    % Output:
    %  H - Spectral entropy

    %normalization
    P=PSD./sum(PSD);
    
    %calculate the entropy
    H = -sum(P.*log(P))/sf;

end

