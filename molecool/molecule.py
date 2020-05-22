from .measure import calculate_distance
def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """calculate bonds in a molecule based on a distance criteria.

    the pairwise distance between atoms is computed. If it is in the range 'min_bond' to 'max_bond', the atoms are counted as     bonded.

    Parameters
    ----------
    coordinates:np.ndarray
        the coordinate of the atoms.
    max_bond : float(optional)
        the max distance for two atom to be consider bonded. the default is 1.5
    min_bond: float(optional)
        the in distance for two point to be considered bonded. the default is 0.

    Returns
    --------
    bonds: dict
        a disctionary where the keys are tuples of bonded atom indices, and the associated values are the bond lengths.
    
    """

    if min_bond <0:
        raise ValueError(F"{min_bond} entered for minimum bond length. minimum bond length can not be less than ZERO!")

    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

