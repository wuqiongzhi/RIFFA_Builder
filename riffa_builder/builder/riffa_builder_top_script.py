#!/usr/bin/python
# Filename : riffa_builder_top_script.py

print ('RIFFA Builder 0.1')

from riffa_builder import RiffaBuilder

bld = RiffaBuilder()

#######################################################################
#User options begin
#Please edit these options for you design
bld.output_dir = 'C:/VSPrj/RIFFA_BUILDER/user/W2'
bld.verilog_src_file = 'C:/VSPrj/RIFFA_BUILDER/user/HLS/HLS_TEST2/solution1/impl/verilog/func.v'
bld.prj_start = 'Verilog'
bld.create_fpga = True
bld.copy_fpga_template = False
bld.fpga_board_name = 'VC709'
bld.fpga_template_name = 'VC709_Gen3x4If128'
bld.clk_div = 2
bld.external_prefixs = []
bld.create_host = True
bld.copy_host_template = True
bld.host_os = 'windows'
bld.host_platform = 'x86'
bld.host_template_type = 'Common'
bld.port_atrbs = [ \
    'func data1 int 1000 debug', \
    'func data2 int 1000 debug',\
    'func data3 int 1000 debug',\
    'func data4 int 1000 debug']
bld.host_debug_level = 3
bld.hardware_timeout = 10000
#User options end
#######################################################################


if ('cancel' in bld.user_wizard()):
    print('Quit')
    sys.exit()


bld.build_fpga_project()
bld.build_host_project()
