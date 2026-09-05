test_exp = [
    ("[empty]", "[empty]"),
    ("[-infinity,0.0]", "[0.0,1.0]"),
    ("[-infinity,-0.0]", "[0.0,1.0]"),
    ("[0.0,infinity]", "[1.0,infinity]"),
    ("[-0.0,infinity]", "[1.0,infinity]"),
    ("[entire]", "[0.0,infinity]"),
    ("[-infinity,0X1.62E42FEFA39FP+9]", "[0.0,infinity]"),
    ("[0X1.62E42FEFA39FP+9,0X1.62E42FEFA39FP+9]", "[0X1.FFFFFFFFFFFFFP+1023,infinity]"),
    ("[0.0,0X1.62E42FEFA39EP+9]", "[1.0,0X1.FFFFFFFFFC32BP+1023]"),
    ("[-0.0,0X1.62E42FEFA39EP+9]", "[1.0,0X1.FFFFFFFFFC32BP+1023]"),
    ("[-0X1.6232BDD7ABCD3P+8,0X1.62E42FEFA39EP+9]", "[0X1.FFFFFFFFFFE7BP-512,0X1.FFFFFFFFFC32BP+1023]"),
    ("[-0X1.6232BDD7ABCD3P+8,0.0]", "[0X1.FFFFFFFFFFE7BP-512,1.0]"),
    ("[-0X1.6232BDD7ABCD3P+8,-0.0]", "[0X1.FFFFFFFFFFE7BP-512,1.0]"),
    ("[-0X1.6232BDD7ABCD3P+8,1.0]", "[0X1.FFFFFFFFFFE7BP-512,0X1.5BF0A8B14576AP+1]"),
    ("[1.0,5.0]", "[0X1.5BF0A8B145769P+1,0X1.28D389970339P+7]"),
    ("[-0X1.A934F0979A372P+1,0X1.CEAECFEA8085AP+0]", "[0X1.2797F0A337A5FP-5,0X1.86091CC9095C5P+2]"),
    ("[0X1.87F42B972949CP-1,0X1.8B55484710029P+6]", "[0X1.1337E9E45812AP+1,0X1.805A5C88021B6P+142]"),
    ("[0X1.78025C8B3FD39P+3,0X1.9FD8EEF3FA79BP+4]", "[0X1.EF461A783114CP+16,0X1.691D36C6B008CP+37]")
]

test_exp_dec = [
    ("[0X1.62E42FEFA39FP+9,0X1.62E42FEFA39FP+9]_com", "[0X1.FFFFFFFFFFFFFP+1023,infinity]_dac"),
    ("[0.0,0X1.62E42FEFA39EP+9]_def", "[1.0,0X1.FFFFFFFFFC32BP+1023]_def")
]

test_exp2 = [
    ("[empty]", "[empty]"),
    ("[-infinity,0.0]", "[0.0,1.0]"),
    ("[-infinity,-0.0]", "[0.0,1.0]"),
    ("[0.0,infinity]", "[1.0,infinity]"),
    ("[-0.0,infinity]", "[1.0,infinity]"),
    ("[entire]", "[0.0,infinity]"),
    ("[-infinity,1024.0]", "[0.0,infinity]"),
    ("[1024.0,1024.0]", "[0X1.FFFFFFFFFFFFFP+1023,infinity]"),
    ("[0.0,1023.0]", "[1.0,0X1P+1023]"),
    ("[-0.0,1023.0]", "[1.0,0X1P+1023]"),
    ("[-1022.0,1023.0]", "[0X1P-1022,0X1P+1023]"),
    ("[-1022.0,0.0]", "[0X1P-1022,1.0]"),
    ("[-1022.0,-0.0]", "[0X1P-1022,1.0]"),
    ("[-1022.0,1.0]", "[0X1P-1022,2.0]"),
    ("[1.0,5.0]", "[2.0,32.0]"),
    ("[-0X1.A934F0979A372P+1,0X1.CEAECFEA8085AP+0]", "[0X1.9999999999998P-4,0X1.C000000000001P+1]"),
    ("[0X1.87F42B972949CP-1,0X1.8B55484710029P+6]", "[0X1.B333333333332P+0,0X1.C81FD88228B4FP+98]"),
    ("[0X1.78025C8B3FD39P+3,0X1.9FD8EEF3FA79BP+4]", "[0X1.AEA0000721857P+11,0X1.FCA0555555559P+25]")
]

test_exp2_dec = [
    ("[1024.0,1024.0]_com", "[0X1.FFFFFFFFFFFFFP+1023,infinity]_dac"),
    ("[0X1.87F42B972949CP-1,0X1.8B55484710029P+6]_def", "[0X1.B333333333332P+0,0X1.C81FD88228B4FP+98]_def")
]

test_exp10 = [
    ("[empty]", "[empty]"),
    ("[-infinity,0.0]", "[0.0,1.0]"),
    ("[-infinity,-0.0]", "[0.0,1.0]"),
    ("[0.0,infinity]", "[1.0,infinity]"),
    ("[-0.0,infinity]", "[1.0,infinity]"),
    ("[entire]", "[0.0,infinity]"),
    ("[-infinity,0X1.34413509F79FFP+8]", "[0.0,infinity]"),
    ("[0X1.34413509F79FFP+8,0X1.34413509F79FFP+8]", "[0X1.FFFFFFFFFFFFFP+1023,infinity]"),
    ("[0.0,0X1.34413509F79FEP+8]", "[1.0,0X1.FFFFFFFFFFBA1P+1023]"),
    ("[-0.0,0X1.34413509F79FEP+8]", "[1.0,0X1.FFFFFFFFFFBA1P+1023]"),
    ("[-0X1.33A7146F72A42P+8,0X1.34413509F79FEP+8]", "[0X0.FFFFFFFFFFFE3P-1022,0X1.FFFFFFFFFFBA1P+1023]"),
    ("[-0X1.22P+7,0X1.34413509F79FEP+8]", "[0X1.3FAAC3E3FA1F3P-482,0X1.FFFFFFFFFFBA1P+1023]"),
    ("[-0X1.22P+7,0.0]", "[0X1.3FAAC3E3FA1F3P-482,1.0]"),
    ("[-0X1.22P+7,-0.0]", "[0X1.3FAAC3E3FA1F3P-482,1.0]"),
    ("[-0X1.22P+7,1.0]", "[0X1.3FAAC3E3FA1F3P-482,10.0]"),
    ("[1.0,5.0]", "[10.0,100000.0]"),
    ("[-0X1.A934F0979A372P+1,0X1.CEAECFEA8085AP+0]", "[0X1.F3A8254311F9AP-12,0X1.00B18AD5B7D56P+6]"),
    ("[0X1.87F42B972949CP-1,0X1.8B55484710029P+6]", "[0X1.75014B7296807P+2,0X1.3EEC1D47DFB2BP+328]"),
    ("[0X1.78025C8B3FD39P+3,0X1.9FD8EEF3FA79BP+4]", "[0X1.0608D2279A811P+39,0X1.43AF5D4271CB8P+86]")
]

test_exp10_dec = [
    ("[0X1.34413509F79FFP+8,0X1.34413509F79FFP+8]_com", "[0X1.FFFFFFFFFFFFFP+1023,infinity]_dac"),
    ("[0X1.87F42B972949CP-1,0X1.8B55484710029P+6]_def", "[0X1.75014B7296807P+2,0X1.3EEC1D47DFB2BP+328]_def")
]

test_log = [
    ("[empty]", "[empty]"),
    ("[-infinity,0.0]", "[empty]"),
    ("[-infinity,-0.0]", "[empty]"),
    ("[0.0,1.0]", "[-infinity,0.0]"),
    ("[-0.0,1.0]", "[-infinity,0.0]"),
    ("[1.0,infinity]", "[0.0,infinity]"),
    ("[0.0,infinity]", "[entire]"),
    ("[-0.0,infinity]", "[entire]"),
    ("[entire]", "[entire]"),
    ("[0.0,0x1.FFFFFFFFFFFFFp1023]", "[-infinity,0X1.62E42FEFA39FP+9]"),
    ("[-0.0,0x1.FFFFFFFFFFFFFp1023]", "[-infinity,0X1.62E42FEFA39FP+9]"),
    ("[1.0,0x1.FFFFFFFFFFFFFp1023]", "[0.0,0X1.62E42FEFA39FP+9]"),
    ("[0x0.0000000000001p-1022,0x1.FFFFFFFFFFFFFp1023]", "[-0x1.74385446D71C4p9, +0x1.62E42FEFA39Fp9]"),
    ("[0x0.0000000000001p-1022,1.0]", "[-0x1.74385446D71C4p9,0.0]"),
    ("[0X1.5BF0A8B145769P+1,0X1.5BF0A8B145769P+1]", "[0X1.FFFFFFFFFFFFFP-1,0X1P+0]"),
    ("[0X1.5BF0A8B14576AP+1,0X1.5BF0A8B14576AP+1]", "[0X1P+0,0X1.0000000000001P+0]"),
    ("[0x0.0000000000001p-1022,0X1.5BF0A8B14576AP+1]", "[-0x1.74385446D71C4p9,0X1.0000000000001P+0]"),
    ("[0X1.5BF0A8B145769P+1,32.0]", "[0X1.FFFFFFFFFFFFFP-1,0X1.BB9D3BEB8C86CP+1]"),
    ("[0X1.999999999999AP-4,0X1.CP+1]", "[-0X1.26BB1BBB55516P+1,0X1.40B512EB53D6P+0]"),
    ("[0X1.B333333333333P+0,0X1.C81FD88228B2FP+98]", "[0X1.0FAE81914A99P-1,0X1.120627F6AE7F1P+6]"),
    ("[0X1.AEA0000721861P+11,0X1.FCA055555554CP+25]", "[0X1.04A1363DB1E63P+3,0X1.203E52C0256B5P+4]")
]

test_log_dec = [
    ("[0x0.0000000000001p-1022,0x1.FFFFFFFFFFFFFp1023]_com", "[-0x1.74385446D71C4p9,0X1.62E42FEFA39FP+9]_com"),
    ("[0.0,1.0]_com", "[-infinity,0.0]_trv"),
    ("[0X1.5BF0A8B14576AP+1,0X1.5BF0A8B14576AP+1]_def", "[0X1P+0,0X1.0000000000001P+0]_def")
]

test_log2 = [
    ("[empty]", "[empty]"),
    ("[-infinity,0.0]", "[empty]"),
    ("[-infinity,-0.0]", "[empty]"),
    ("[0.0,1.0]", "[-infinity,0.0]"),
    ("[-0.0,1.0]", "[-infinity,0.0]"),
    ("[1.0,infinity]", "[0.0,infinity]"),
    ("[0.0,infinity]", "[entire]"),
    ("[-0.0,infinity]", "[entire]"),
    ("[entire]", "[entire]"),
    ("[0.0,0x1.FFFFFFFFFFFFFp1023]", "[-infinity,1024.0]"),
    ("[-0.0,0x1.FFFFFFFFFFFFFp1023]", "[-infinity,1024.0]"),
    ("[1.0,0x1.FFFFFFFFFFFFFp1023]", "[0.0,1024.0]"),
    ("[0x0.0000000000001p-1022,0x1.FFFFFFFFFFFFFp1023]", "[-1074.0,1024.0]"),
    ("[0x0.0000000000001p-1022,1.0]", "[-1074.0,0.0]"),
    ("[0x0.0000000000001p-1022,2.0]", "[-1074.0,1.0]"),
    ("[2.0,32.0]", "[1.0,5.0]"),
    ("[0X1.999999999999AP-4,0X1.CP+1]", "[-0X1.A934F0979A372P+1,0X1.CEAECFEA8085AP+0]"),
    ("[0X1.B333333333333P+0,0X1.C81FD88228B2FP+98]", "[0X1.87F42B972949CP-1,0X1.8B55484710029P+6]"),
    ("[0X1.AEA0000721861P+11,0X1.FCA055555554CP+25]", "[0X1.78025C8B3FD39P+3,0X1.9FD8EEF3FA79BP+4]")
]

test_log2_dec = [
    ("[0x0.0000000000001p-1022,0x1.FFFFFFFFFFFFFp1023]_com", "[-1074.0,1024.0]_com"),
    ("[0x0.0000000000001p-1022,infinity]_dac", "[-1074.0,infinity]_dac"),
    ("[2.0,32.0]_def", "[1.0,5.0]_def"),
    ("[0.0,0x1.FFFFFFFFFFFFFp1023]_com", "[-infinity,1024.0]_trv")
]

test_log10 = [
    ("[empty]", "[empty]"),
    ("[-infinity,0.0]", "[empty]"),
    ("[-infinity,-0.0]", "[empty]"),
    ("[0.0,1.0]", "[-infinity,0.0]"),
    ("[-0.0,1.0]", "[-infinity,0.0]"),
    ("[1.0,infinity]", "[0.0,infinity]"),
    ("[0.0,infinity]", "[entire]"),
    ("[-0.0,infinity]", "[entire]"),
    ("[entire]", "[entire]"),
    ("[0.0,0x1.FFFFFFFFFFFFFp1023]", "[-infinity,0X1.34413509F79FFP+8]"),
    ("[-0.0,0x1.FFFFFFFFFFFFFp1023]", "[-infinity,0X1.34413509F79FFP+8]"),
    ("[1.0,0x1.FFFFFFFFFFFFFp1023]", "[0.0,0X1.34413509F79FFP+8]"),
    ("[0x0.0000000000001p-1022,0x1.FFFFFFFFFFFFFp1023]", "[-0x1.434E6420F4374p+8, +0x1.34413509F79FFp+8]"),
    ("[0x0.0000000000001p-1022,1.0]", "[-0x1.434E6420F4374p+8,0.0]"),
    ("[0x0.0000000000001p-1022,10.0]", "[-0x1.434E6420F4374p+8,1.0]"),
    ("[10.0,100000.0]", "[1.0,5.0]"),
    ("[0X1.999999999999AP-4,0X1.CP+1]", "[-0X1P+0,0X1.1690163290F4P-1]"),
    ("[0X1.999999999999AP-4,0X1.999999999999AP-4]", "[-0X1P+0,-0X1.FFFFFFFFFFFFFP-1]"),
    ("[0X1.B333333333333P+0,0X1.C81FD88228B2FP+98]", "[0X1.D7F59AA5BECB9P-3,0X1.DC074D84E5AABP+4]"),
    ("[0X1.AEA0000721861P+11,0X1.FCA055555554CP+25]", "[0X1.C4C29DD829191P+1,0X1.F4BAEBBA4FA4P+2]")
]

test_log10_dec = [
    ("[0x0.0000000000001p-1022,0x1.FFFFFFFFFFFFFp1023]_com", "[-0x1.434E6420F4374p+8,0X1.34413509F79FFP+8]_com"),
    ("[0.0,0x1.FFFFFFFFFFFFFp1023]_dac", "[-infinity,0X1.34413509F79FFP+8]_trv")
]
