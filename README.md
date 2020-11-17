# Analog-Notch-Filter-Design-
The following is a Jupyter notebook that carries out a notch filter design as described in the Linear Circuit Design Handbook. The same approach can be used to design other filter topologies, such as low-pass, high-pass, and band-pass. The implementation is focused on a Bainter topology, but can be extended by changing the design equations to a different topology. 

The benefit of taking a fundamental approach, is it more easily allows the individual stages to be inspected during the debugging process, individual passive values to be 'tweaked' based on actual part availability, and a more thorough understanding of the filter implementation to be achieved. 

This function can be used by pulling the notebook, updating the desired characteristics in section 3., and executing the notebook. Actual measured values can be added in additional plots to be compared to the theoretical response. 

Section 7 can be used when inspecting magnitudes of attenuation at particular frequencies. 
