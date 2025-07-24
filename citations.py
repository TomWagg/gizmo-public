import argparse

tags_from_keywords = [
    {
        "AnglesAlcazar2016": ["BH_GRAVACCRETION", "BH_WIND_KICK"],
        "AnglesAlcazar2017": ["BH_OUTPUT_MOREINFO", "BH_SEED_FROM_FOF"],
        "Bauer2012": ["TURB_DRIVING", "TURB_DRIVING_SPECTRUMGRID"],
        "Chan2019": ["COSMIC_RAY_FLUID", "CRFLUID_ALT_FLUX_FORM_JOCH", "CRFLUID_ALT_RSOL_FORM", "CRFLUID_DIFFUSION_MODEL", "CRFLUID_EVOLVE_SCATTERINGWAVES", "CRFLUID_EVOLVE_SPECTRUM", "CRFLUID_ION_ALFVEN_SPEED", "CRFLUID_M1"],
        "Clark2011": ["RT_USE_TREECOL_FOR_NH"],
        "Deng2017": ["EOS_TILLOTSON"],
        "Garrison_Kimmel2017": ["BH_CALC_DISTANCES"],
        "Gnedin2001a": ["RT_OTVET"],
        "Grudic2018": ["GALSF_SFR_VIRIAL_SF_CRITERION"],
        "Grudic2021": ["EOS_SUBSTELLAR_ISM", "GALSF_SFR_CRITERION", "HERMITE_INTEGRATION", "MAINTAIN_TREE_IN_REARRANGE", "RANDOMIZE_GRAVTREE", "RT_BH_ANGLEWEIGHT_PHOTON_INJECTION", "RT_REPROCESS_INJECTED_PHOTONS", "SINGLE_STAR_ACCRETION", "SINGLE_STAR_FB_JETS", "SINGLE_STAR_FB_RAD", "SINGLE_STAR_FB_SNE", "SINGLE_STAR_FB_WINDS", "SINGLE_STAR_FIND_BINARIES", "SINGLE_STAR_SINK_FORMATION", "SINGLE_STAR_STARFORGE_PROTOSTELLAR_EVOLUTION", "SINGLE_STAR_TIMESTEPPING"],
        "Grudic2021a": ["ADAPTIVE_TREEFORCE_UPDATE"],
        "Guszejnov2017": ["GALSF_SFR_IMF_VARIATION"],
        "Hopkins2011": ["BH_GRAVACCRETION", "BH_SUBGRIDBHVARIABILITY"],
        "Hopkins2012": ["RT_LEBRON"],
        "Hopkins2013": ["GALSF_SFR_VIRIAL_SF_CRITERION"],
        "Hopkins2014a": ["DM_SCALARFIELD_SCREENING"],
        "Hopkins2015": ["MAGNETIC", "MHD_B_SET_IN_PARAMS", "MHD_CONSTRAINED_GRADIENT", "MHD_NON_IDEAL"],
        "Hopkins2016": ["GRAIN_BACKREACTION", "GRAIN_COLLISIONS", "GRAIN_EPSTEIN_STOKES", "GRAIN_FLUID", "GRAIN_LORENTZFORCE", "GRAIN_RDI_TESTPROBLEM"],
        "Hopkins2016a": ["BH_COMPTON_HEATING", "BH_GRAVCAPTURE_GAS", "BH_GRAVCAPTURE_NONGAS", "BH_WIND_CONTINUOUS"],
        "Hopkins2016b": ["MHD_CONSTRAINED_GRADIENT"],
        "Hopkins2016c": ["CONDUCTION", "MHD_NON_IDEAL", "VISCOSITY"],
        "Hopkins2017": ["ADAPTIVE_GRAVSOFT_FORALL", "COOLING", "COOL_LOW_TEMPERATURES", "COOL_METAL_LINES_BY_SPECIES", "COOL_MOLECFRAC", "COOL_UVB_SELFSHIELD_RAHMATI", "FIRE_PHYSICS_DEFAULTS", "FIRE_SUPERLAGRANGIAN_JEANS_REFINEMENT", "GALSF_SFR_MOLECULAR_CRITERION", "METALS", "RT_LEBRON", "TURB_DIFF_DYNAMIC", "TURB_DIFF_ENERGY", "TURB_DIFF_METALS", "TURB_DIFF_VELOCITY"],
        "Hopkins2018": ["GALSF_FB_MECHANICAL"],
        "Hopkins2018a": ["RT_FLUXLIMITEDDIFFUSION", "RT_LEBRON", "RT_LOCALRAYGRID", "RT_M1", "RT_OTVET"],
        "Hopkins2019": ["DM_FUZZY"],
        "Hopkins2019a": ["RT_CHEM_PHOTOION", "RT_FREEFREE", "RT_GENERIC_USER_FREQ", "RT_INFRARED", "RT_LYMAN_WERNER", "RT_NUV", "RT_OPACITY_FROM_EXPLICIT_GRAINS", "RT_OPTICAL_NIR", "RT_PHOTOELECTRIC", "RT_XRAY"],
        "Hopkins2019b": ["COSMIC_RAY_FLUID", "CRFLUID_ALT_FLUX_FORM_JOCH", "CRFLUID_ALT_RSOL_FORM", "CRFLUID_DIFFUSION_MODEL", "CRFLUID_EVOLVE_SCATTERINGWAVES", "CRFLUID_EVOLVE_SPECTRUM", "CRFLUID_ION_ALFVEN_SPEED", "CRFLUID_M1"],
        "Hopkins2020": ["CRFLUID_ION_ALFVEN_SPEED", "CR_FLUID_DIFFUSION_MODEL"],
        "Hopkins2021": ["BH_GRAVACCRETION_STELLARFBCORR", "COSMIC_RAY_FLUID", "CRFLUID_ALT_RSOL_FORM", "CRFLUID_ALT_VARIABLE_RSOL", "CRFLUID_DIFFUSION_MODEL", "CRFLUID_EVOLVE_SCATTERINGWAVES", "CRFLUID_EVOLVE_SPECTRUM", "CRFLUID_ION_ALFVEN_SPEED", "CRFLUID_M1"],
        "Hopkins2022": ["COSMIC_RAY_FLUID", "CRFLUID_ALT_FLUX_FORM_JOCH", "CRFLUID_ALT_RSOL_FORM", "CRFLUID_DIFFUSION_MODEL", "CRFLUID_EVOLVE_SCATTERINGWAVES", "CRFLUID_EVOLVE_SPECTRUM", "CRFLUID_ION_ALFVEN_SPEED", "CRFLUID_M1"],
        "Hopkins2022a": ["RT_OPACITY_FROM_EXPLICIT_GRAINS"],
        "Hopkins2022b": ["CRFLUID_ION_ALFVEN_SPEED", "CR_FLUID_DIFFUSION_MODEL"],
        "Hopkins2022c": ["CR_FLUID_EVOLVE_SPECTRUM"],
        "Hopkins2022d": ["COOL_LOW_TEMPERATURES", "COOL_MOLECFRAC", "COOL_UVB_SELFSHIELD_RAHMATI", "GALSF_FB_FIRE_AGE_TRACERS"],
        "Hopkins2023": ["COSMIC_RAY_SUBGRID_LEBRON"],
        "Hopkins2023a": ["ADAPTIVE_GRAVSOFT_FROM_TIDAL_CRITERION"],
        "Ji2022": ["GRAIN_FLUID_AND_PIC_BOTH_DEFINED", "PIC_MHD"],
        "Ji2022a": ["PIC_SPEEDOFLIGHT_REDUCTION"],
        "Jiang2014": ["RT_LOCALRAYGRID"],
        "Khurshudyan2016": ["TURB_DIFF_ENERGY", "TURB_DIFF_METALS", "TURB_DIFF_VELOCITY"],
        "Lane2021": ["GRAVITY_SPHERICAL_SYMMETRY"],
        "Lee2017": ["GRAIN_BACKREACTION", "GRAIN_COLLISIONS", "GRAIN_EPSTEIN_STOKES", "GRAIN_FLUID", "GRAIN_LORENTZFORCE", "GRAIN_RDI_TESTPROBLEM"],
        "Ma2021": ["BH_DYNfRICTION_FROMTREE"],
        "Ma2023": ["BH_DYNfRICTION_FROMTREE"],
        "Moseley2019": ["GRAIN_BACKREACTION", "GRAIN_FLUID", "GRAIN_RDI_TESTPROBLEM"],
        "Oppenheimer2006": ["GALSF_SUBGRID_WIND_SCALING", "GALSF_WINDS_ORIENTATION"],
        "Petkova2009": ["RT_DIFFUSION_IMPLICIT"],
        "Reinhardt2017": ["EOS_TILLOTSON"],
        "Rennehan2018": ["TURB_DIFF_DYNAMIC"],
        "Rennehan2021": ["TURB_DIFF_DYNAMIC"],
        "Richings2014": ["CHIMES"],
        "Richings2014a": ["CHIMES"],
        "Robertson2008": ["EOS_TRUELOVE_PRESSURE"],
        "Robles2017": ["DM_SIDM"],
        "Rocha2013": ["DM_SIDM"],
        "Rosdahl2013": ["RT_M1"],
        "Springel2001": ["FOF", "FOF_DENSITY_SPLIT_TYPES", "FOF_GROUP_MIN_SIZE", "FOF_PRIMARY_LINK_TYPES", "FOF_SECONDARY_LINK_TYPES", "SUBFIND", "SUBFIND_ADDIO_BARYONS", "SUBFIND_ADDIO_NUMOVERDEN", "SUBFIND_ADDIO_VELDISP", "SUBFIND_REMOVE_GAS_STRUCTURES", "SUBFIND_SAVE_PARTICLEDATA"],
        "Springel2003": ["GALSF", "GALSF_EFFECTIVE_EQS", "GALSF_SUBGRID_WINDS", "GALSF_SUBGRID_WIND_SCALING"],
        "Springel2005": ["BH_BONDI", "BH_DRAG", "BH_THERMALFEEDBACK"],
        "Stinson2006": ["GALSF_FB_TURNOFF_COOLING"],
        "Su2017": ["CONDUCTION_SPITZER", "VISCOSITY_BRAGINSKII"],
        "Su2018": ["GALSF_SFR_IMF_SAMPLING"],
        "Su2021": ["BH_DEBUG_FIX_MDOT_MBH", "BH_DEBUG_SPAWN_JET_TEST", "BH_WIND_SPAWN_SET_BFIELD_POLTOR", "BH_WIND_SPAWN_SET_JET_PRECESSION", "SINGLE_STAR_FB_JETS"],
        "Tremmel2015": ["BH_DYNFRICTION"],
        "Weinberger2020": ["SUBFIND", "SUBFIND_ADDIO_BARYONS", "SUBFIND_ADDIO_NUMOVERDEN", "SUBFIND_ADDIO_VELDISP", "SUBFIND_REMOVE_GAS_STRUCTURES", "SUBFIND_SAVE_PARTICLEDATA"],
        "Wellons2023": ["BH_BONDI", "BH_DRAG", "BH_THERMALFEEDBACK"],
        "Wiersma2009": ["COOL_METAL_LINES_BY_SPECIES"],
        "Zhu2016": ["GALSF_SUBGRID_WIND_SCALING", "GALSF_WINDS_ORIENTATION"],
    }
]

def get_citation_tags_from_config(filepath):
    """Retrieve a list of BiBTeX citation tags based on the settings specified in a configuration file.

    Parameters
    ----------
    filepath : `str`
        Path to the configuration file.

    Returns
    -------
    citations : `list`
        List of BiBTeX citation tags that correspond to the settings in the configuration file.
    """

    # check which settings are turned on in the config file
    settings_on = set()
    with open(filepath, 'r') as file:
        # go through each line
        for line in file:
            # find any lines that aren't blank/comments
            if not line.strip().startswith("#") and len(line.strip()) > 0:
                # take just the initial setting name, remove anything after an equals sign
                setting = line.strip().split(" ")[0]
                setting = setting.split("=")[0] if "=" in setting else setting
                settings_on.add(setting)

    # track which tags are relevant based on the settings    
    citation_tags = set()
    for mapper in tags_from_keywords:
        for tag, keywords in mapper.items():
            if len(set(keywords).intersection(settings_on)) > 0:
                citation_tags.add(tag)

    return sorted(list(citation_tags))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get citation tags based on a configuration file.")
    parser.add_argument("--filepath", "-f", required=True,
                        type=str, help="Path to the configuration file.")
    args = parser.parse_args()

    citation_tags = get_citation_tags_from_config(args.filepath)
    acknowledgement = "This work makes use of the GIZMO code \\citep{Hopkins2014, Springel2005}."

    if len(citation_tags) > 0:
        acknowledgement += " GIZMO simulations in this study were run with additional features, which are based on a variety of other works \\citep{" + ", ".join(citation_tags) + "}."

    print(acknowledgement)
