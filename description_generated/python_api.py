import xlwings as xw
addin_name_str = "C:\\Users\\olegk\\Documents\\unifloc_vba\\UniflocVBA_7.xlam"
class API():
    def __init__(self, addin_name_str):
        book = xw.Book(addin_name_str)
        self.PVT_bg_m3m3 = book.macro("PVT_bg_m3m3")
        self.PVT_bo_m3m3 = book.macro("PVT_bo_m3m3")
        self.PVT_bw_m3m3 = book.macro("PVT_bw_m3m3")
        self.PVT_salinity_ppm = book.macro("PVT_salinity_ppm")
        self.PVT_mu_oil_cP = book.macro("PVT_mu_oil_cP")
        self.PVT_mu_gas_cP = book.macro("PVT_mu_gas_cP")
        self.PVT_mu_wat_cP = book.macro("PVT_mu_wat_cP")
        self.PVT_rs_m3m3 = book.macro("PVT_rs_m3m3")
        self.PVT_z = book.macro("PVT_z")
        self.PVT_rhoo_kgm3 = book.macro("PVT_rhoo_kgm3")
        self.PVT_rhog_kgm3 = book.macro("PVT_rhog_kgm3")
        self.PVT_rhow_kgm3 = book.macro("PVT_rhow_kgm3")
        self.PVT_pb_atma = book.macro("PVT_pb_atma")
        self.PVT_SToilgas_Nm = book.macro("PVT_SToilgas_Nm")
        self.PVT_STwatgas_Nm = book.macro("PVT_STwatgas_Nm")
        self.PVT_STliqgas_Nm = book.macro("PVT_STliqgas_Nm")
        self.MF_CJT_Katm = book.macro("MF_CJT_Katm")
        self.MF_q_mix_rc_m3day = book.macro("MF_q_mix_rc_m3day")
        self.MF_rhomix_kgm3 = book.macro("MF_rhomix_kgm3")
        self.MF_mu_mix_cP = book.macro("MF_mu_mix_cP")
        self.MF_gas_fraction_d = book.macro("MF_gas_fraction_d")
        self.MF_p_gas_fraction_atma = book.macro("MF_p_gas_fraction_atma")
        self.MF_rp_gas_fraction_m3m3 = book.macro("MF_rp_gas_fraction_m3m3")
        self.MF_ksep_natural_d = book.macro("MF_ksep_natural_d")
        self.MF_ksep_total_d = book.macro("MF_ksep_total_d")
        self.MF_ksep_gasseparator_d = book.macro("MF_ksep_gasseparator_d")
        self.MF_gasseparator_name = book.macro("MF_gasseparator_name")
        self.MF_dpdl_atmm = book.macro("MF_dpdl_atmm")
        self.MF_dp_pipe_atm = book.macro("MF_dp_pipe_atm")
        self.MF_calibr_pipe_m3day = book.macro("MF_calibr_pipe_m3day")
        self.MF_p_pipe_atma = book.macro("MF_p_pipe_atma")
        self.MF_p_pipe_znlf_atma = book.macro("MF_p_pipe_znlf_atma")
        self.MF_dp_choke_atm = book.macro("MF_dp_choke_atm")
        self.MF_p_choke_atma = book.macro("MF_p_choke_atma")
        self.MF_calibr_choke_fr = book.macro("MF_calibr_choke_fr")
        self.MF_qliq_choke_sm3day = book.macro("MF_qliq_choke_sm3day")
        self.IPR_qliq_sm3day = book.macro("IPR_qliq_sm3day")
        self.IPR_pwf_atma = book.macro("IPR_pwf_atma")
        self.IPR_pi_sm3dayatm = book.macro("IPR_pi_sm3dayatm")
        self.ESP_head_m = book.macro("ESP_head_m")
        self.ESP_power_W = book.macro("ESP_power_W")
        self.ESP_eff_fr = book.macro("ESP_eff_fr")
        self.ESP_name = book.macro("ESP_name")
        self.ESP_max_rate_m3day = book.macro("ESP_max_rate_m3day")
        self.ESP_optRate_m3day = book.macro("ESP_optRate_m3day")
        self.ESP_id_by_rate = book.macro("ESP_id_by_rate")
        self.ESP_p_atma = book.macro("ESP_p_atma")
        self.ESP_dp_atm = book.macro("ESP_dp_atm")
        self.ESP_calibr_calc = book.macro("ESP_calibr_calc")
        self.ESP_system_calc = book.macro("ESP_system_calc")
        self.motor_M_slip_Nm = book.macro("motor_M_slip_Nm")
        self.motor_I_slip_A = book.macro("motor_I_slip_A")
        self.motor_CosPhi_slip = book.macro("motor_CosPhi_slip")
        self.motor_Eff_slip = book.macro("motor_Eff_slip")
        self.motor_M_Nm = book.macro("motor_M_Nm")
        self.motor_I_A = book.macro("motor_I_A")
        self.motor_CosPhi_d = book.macro("motor_CosPhi_d")
        self.motor_Eff_d = book.macro("motor_Eff_d")
        self.motor_S_d = book.macro("motor_S_d")
        self.motor_Name = book.macro("motor_Name")
        self.motor_Pnom_kW = book.macro("motor_Pnom_kW")
        self.GLV_q_gas_sm3day = book.macro("GLV_q_gas_sm3day")
        self.GLV_q_gas_vkr_sm3day = book.macro("GLV_q_gas_vkr_sm3day")
        self.GLV_p_vkr_atma = book.macro("GLV_p_vkr_atma")
        self.GLV_p_atma = book.macro("GLV_p_atma")
        self.GLV_p_bellow_atma = book.macro("GLV_p_bellow_atma")
        self.GLV_p_close_atma = book.macro("GLV_p_close_atma")
        self.GLV_d_choke_mm = book.macro("GLV_d_choke_mm")
        self.GLV_IPO_p_open = book.macro("GLV_IPO_p_open")
        self.GLV_IPO_p_atma = book.macro("GLV_IPO_p_atma")
        self.GLV_IPO_p_close = book.macro("GLV_IPO_p_close")
        self.PVT_encode_string = book.macro("PVT_encode_string")
        self.PVT_decode_string = book.macro("PVT_decode_string")
        self.well_encode_string = book.macro("well_encode_string")
        self.well_decode_string = book.macro("well_decode_string")
        self.ESP_encode_string = book.macro("ESP_encode_string")
        self.ESP_decode_string = book.macro("ESP_decode_string")
        self.wellGL_decode_string = book.macro("wellGL_decode_string")
        self.wellGL_encode_string = book.macro("wellGL_encode_string")
        self.well_plin_pwf_atma = book.macro("well_plin_pwf_atma")
        self.well_pintake_pwf_atma = book.macro("well_pintake_pwf_atma")
        self.well_pwf_plin_atma = book.macro("well_pwf_plin_atma")
        self.well_calcc_calibr_head_fr = book.macro("well_calcc_calibr_head_fr")
        self.well_pwf_Hdyn_atma = book.macro("well_pwf_Hdyn_atma")
        self.nodal_qliq_sm3day = book.macro("nodal_qliq_sm3day")
        self.crv_interpolation = book.macro("crv_interpolation")
        self.crv_solve = book.macro("crv_solve")
        self.crv_intersection = book.macro("crv_intersection")
UniflocVBA = API(addin_name_str)
print(UniflocVBA.PVT_bo_m3m3(30,30))
