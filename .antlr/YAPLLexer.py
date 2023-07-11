# Generated from c:\Users\cjrba\OneDrive\Documentos\Universidad\2023Parte2\Compiladores\Laboratorio0-GeneracionDeScannerYParser-ConstruccionDeCompiladores\YAPL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0196\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\7\16\u00b5\n\16\f\16\16\16\u00b8\13\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17\u00c2\n\17\f")
        buf.write("\17\16\17\u00c5\13\17\3\17\5\17\u00c8\n\17\3\17\3\17\3")
        buf.write("\20\6\20\u00cd\n\20\r\20\16\20\u00ce\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write("-\3-\7-\u0147\n-\f-\16-\u014a\13-\3.\3.\7.\u014e\n.\f")
        buf.write(".\16.\u0151\13.\3.\3.\3/\3/\7/\u0157\n/\f/\16/\u015a\13")
        buf.write("/\3\60\6\60\u015d\n\60\r\60\16\60\u015e\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3")
        buf.write("@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3")
        buf.write("I\3J\3J\3K\3K\4\u00b6\u014f\2L\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f")
        buf.write("\2\u0091\2\u0093\2\u0095\2\3\2#\3\2\f\f\6\2\13\f\16\17")
        buf.write("\"\"^^\3\2C\\\6\2\62;C\\aac|\3\2c|\3\2\62;\4\2CCcc\4\2")
        buf.write("DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4")
        buf.write("\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQq")
        buf.write("q\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2")
        buf.write("XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\6\2,,\60\60]]_")
        buf.write("_\2\u0183\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\3\u0097\3\2\2\2\5\u0099\3")
        buf.write("\2\2\2\7\u009b\3\2\2\2\t\u009d\3\2\2\2\13\u009f\3\2\2")
        buf.write("\2\r\u00a1\3\2\2\2\17\u00a3\3\2\2\2\21\u00a5\3\2\2\2\23")
        buf.write("\u00a7\3\2\2\2\25\u00a9\3\2\2\2\27\u00ab\3\2\2\2\31\u00ae")
        buf.write("\3\2\2\2\33\u00b1\3\2\2\2\35\u00bd\3\2\2\2\37\u00cc\3")
        buf.write("\2\2\2!\u00d2\3\2\2\2#\u00d8\3\2\2\2%\u00e1\3\2\2\2\'")
        buf.write("\u00e6\3\2\2\2)\u00ec\3\2\2\2+\u00ef\3\2\2\2-\u00f2\3")
        buf.write("\2\2\2/\u00f7\3\2\2\2\61\u00fc\3\2\2\2\63\u00ff\3\2\2")
        buf.write("\2\65\u0105\3\2\2\2\67\u010a\3\2\2\29\u010f\3\2\2\2;\u0113")
        buf.write("\3\2\2\2=\u0116\3\2\2\2?\u011b\3\2\2\2A\u011e\3\2\2\2")
        buf.write("C\u0123\3\2\2\2E\u0126\3\2\2\2G\u012a\3\2\2\2I\u0131\3")
        buf.write("\2\2\2K\u0133\3\2\2\2M\u0135\3\2\2\2O\u0137\3\2\2\2Q\u0139")
        buf.write("\3\2\2\2S\u013d\3\2\2\2U\u013f\3\2\2\2W\u0142\3\2\2\2")
        buf.write("Y\u0144\3\2\2\2[\u014b\3\2\2\2]\u0154\3\2\2\2_\u015c\3")
        buf.write("\2\2\2a\u0160\3\2\2\2c\u0162\3\2\2\2e\u0164\3\2\2\2g\u0166")
        buf.write("\3\2\2\2i\u0168\3\2\2\2k\u016a\3\2\2\2m\u016c\3\2\2\2")
        buf.write("o\u016e\3\2\2\2q\u0170\3\2\2\2s\u0172\3\2\2\2u\u0174\3")
        buf.write("\2\2\2w\u0176\3\2\2\2y\u0178\3\2\2\2{\u017a\3\2\2\2}\u017c")
        buf.write("\3\2\2\2\177\u017e\3\2\2\2\u0081\u0180\3\2\2\2\u0083\u0182")
        buf.write("\3\2\2\2\u0085\u0184\3\2\2\2\u0087\u0186\3\2\2\2\u0089")
        buf.write("\u0188\3\2\2\2\u008b\u018a\3\2\2\2\u008d\u018c\3\2\2\2")
        buf.write("\u008f\u018e\3\2\2\2\u0091\u0190\3\2\2\2\u0093\u0192\3")
        buf.write("\2\2\2\u0095\u0194\3\2\2\2\u0097\u0098\7=\2\2\u0098\4")
        buf.write("\3\2\2\2\u0099\u009a\7}\2\2\u009a\6\3\2\2\2\u009b\u009c")
        buf.write("\7\177\2\2\u009c\b\3\2\2\2\u009d\u009e\7*\2\2\u009e\n")
        buf.write("\3\2\2\2\u009f\u00a0\7.\2\2\u00a0\f\3\2\2\2\u00a1\u00a2")
        buf.write("\7+\2\2\u00a2\16\3\2\2\2\u00a3\u00a4\7<\2\2\u00a4\20\3")
        buf.write("\2\2\2\u00a5\u00a6\7B\2\2\u00a6\22\3\2\2\2\u00a7\u00a8")
        buf.write("\7\60\2\2\u00a8\24\3\2\2\2\u00a9\u00aa\7\u0080\2\2\u00aa")
        buf.write("\26\3\2\2\2\u00ab\u00ac\7*\2\2\u00ac\u00ad\7,\2\2\u00ad")
        buf.write("\30\3\2\2\2\u00ae\u00af\7,\2\2\u00af\u00b0\7+\2\2\u00b0")
        buf.write("\32\3\2\2\2\u00b1\u00b6\5\27\f\2\u00b2\u00b5\5\33\16\2")
        buf.write("\u00b3\u00b5\13\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b9\u00ba\5\31\r\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc")
        buf.write("\b\16\2\2\u00bc\34\3\2\2\2\u00bd\u00be\7/\2\2\u00be\u00bf")
        buf.write("\7/\2\2\u00bf\u00c3\3\2\2\2\u00c0\u00c2\n\2\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3")
        buf.write("\2\2\2\u00c6\u00c8\7\f\2\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\b\17\2\2\u00ca")
        buf.write("\36\3\2\2\2\u00cb\u00cd\t\3\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00d1\b\20\2\2\u00d1 \3\2\2")
        buf.write("\2\u00d2\u00d3\5e\63\2\u00d3\u00d4\5w<\2\u00d4\u00d5\5")
        buf.write("a\61\2\u00d5\u00d6\5\u0085C\2\u00d6\u00d7\5\u0085C\2\u00d7")
        buf.write("\"\3\2\2\2\u00d8\u00d9\5q9\2\u00d9\u00da\5{>\2\u00da\u00db")
        buf.write("\5o8\2\u00db\u00dc\5i\65\2\u00dc\u00dd\5\u0083B\2\u00dd")
        buf.write("\u00de\5q9\2\u00de\u00df\5\u0087D\2\u00df\u00e0\5\u0085")
        buf.write("C\2\u00e0$\3\2\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\5\u0083")
        buf.write("B\2\u00e3\u00e4\5\u0089E\2\u00e4\u00e5\5i\65\2\u00e5&")
        buf.write("\3\2\2\2\u00e6\u00e7\7h\2\2\u00e7\u00e8\5a\61\2\u00e8")
        buf.write("\u00e9\5w<\2\u00e9\u00ea\5\u0085C\2\u00ea\u00eb\5i\65")
        buf.write("\2\u00eb(\3\2\2\2\u00ec\u00ed\7>\2\2\u00ed\u00ee\7/\2")
        buf.write("\2\u00ee*\3\2\2\2\u00ef\u00f0\5q9\2\u00f0\u00f1\5k\66")
        buf.write("\2\u00f1,\3\2\2\2\u00f2\u00f3\5i\65\2\u00f3\u00f4\5w<")
        buf.write("\2\u00f4\u00f5\5\u0085C\2\u00f5\u00f6\5i\65\2\u00f6.\3")
        buf.write("\2\2\2\u00f7\u00f8\5\u0087D\2\u00f8\u00f9\5o8\2\u00f9")
        buf.write("\u00fa\5i\65\2\u00fa\u00fb\5{>\2\u00fb\60\3\2\2\2\u00fc")
        buf.write("\u00fd\5k\66\2\u00fd\u00fe\5q9\2\u00fe\62\3\2\2\2\u00ff")
        buf.write("\u0100\5\u008dG\2\u0100\u0101\5o8\2\u0101\u0102\5q9\2")
        buf.write("\u0102\u0103\5w<\2\u0103\u0104\5i\65\2\u0104\64\3\2\2")
        buf.write("\2\u0105\u0106\5w<\2\u0106\u0107\5}?\2\u0107\u0108\5}")
        buf.write("?\2\u0108\u0109\5\177@\2\u0109\66\3\2\2\2\u010a\u010b")
        buf.write("\5\177@\2\u010b\u010c\5}?\2\u010c\u010d\5}?\2\u010d\u010e")
        buf.write("\5w<\2\u010e8\3\2\2\2\u010f\u0110\5w<\2\u0110\u0111\5")
        buf.write("i\65\2\u0111\u0112\5\u0087D\2\u0112:\3\2\2\2\u0113\u0114")
        buf.write("\5q9\2\u0114\u0115\5{>\2\u0115<\3\2\2\2\u0116\u0117\5")
        buf.write("e\63\2\u0117\u0118\5a\61\2\u0118\u0119\5\u0085C\2\u0119")
        buf.write("\u011a\5i\65\2\u011a>\3\2\2\2\u011b\u011c\5}?\2\u011c")
        buf.write("\u011d\5k\66\2\u011d@\3\2\2\2\u011e\u011f\5i\65\2\u011f")
        buf.write("\u0120\5\u0085C\2\u0120\u0121\5a\61\2\u0121\u0122\5e\63")
        buf.write("\2\u0122B\3\2\2\2\u0123\u0124\7?\2\2\u0124\u0125\7@\2")
        buf.write("\2\u0125D\3\2\2\2\u0126\u0127\5{>\2\u0127\u0128\5i\65")
        buf.write("\2\u0128\u0129\5\u008dG\2\u0129F\3\2\2\2\u012a\u012b\5")
        buf.write("q9\2\u012b\u012c\5\u0085C\2\u012c\u012d\5\u008bF\2\u012d")
        buf.write("\u012e\5}?\2\u012e\u012f\5q9\2\u012f\u0130\5g\64\2\u0130")
        buf.write("H\3\2\2\2\u0131\u0132\7-\2\2\u0132J\3\2\2\2\u0133\u0134")
        buf.write("\7/\2\2\u0134L\3\2\2\2\u0135\u0136\7,\2\2\u0136N\3\2\2")
        buf.write("\2\u0137\u0138\7\61\2\2\u0138P\3\2\2\2\u0139\u013a\5{")
        buf.write(">\2\u013a\u013b\5}?\2\u013b\u013c\5\u0087D\2\u013cR\3")
        buf.write("\2\2\2\u013d\u013e\7>\2\2\u013eT\3\2\2\2\u013f\u0140\7")
        buf.write(">\2\2\u0140\u0141\7?\2\2\u0141V\3\2\2\2\u0142\u0143\7")
        buf.write("?\2\2\u0143X\3\2\2\2\u0144\u0148\t\4\2\2\u0145\u0147\t")
        buf.write("\5\2\2\u0146\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149Z\3\2\2\2\u014a\u0148")
        buf.write("\3\2\2\2\u014b\u014f\7$\2\2\u014c\u014e\13\2\2\2\u014d")
        buf.write("\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u014f\u014d\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3")
        buf.write("\2\2\2\u0152\u0153\7$\2\2\u0153\\\3\2\2\2\u0154\u0158")
        buf.write("\t\6\2\2\u0155\u0157\t\5\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159^\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015d\t\7\2")
        buf.write("\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f`\3\2\2\2\u0160\u0161")
        buf.write("\t\b\2\2\u0161b\3\2\2\2\u0162\u0163\t\t\2\2\u0163d\3\2")
        buf.write("\2\2\u0164\u0165\t\n\2\2\u0165f\3\2\2\2\u0166\u0167\t")
        buf.write("\13\2\2\u0167h\3\2\2\2\u0168\u0169\t\f\2\2\u0169j\3\2")
        buf.write("\2\2\u016a\u016b\t\r\2\2\u016bl\3\2\2\2\u016c\u016d\t")
        buf.write("\16\2\2\u016dn\3\2\2\2\u016e\u016f\t\17\2\2\u016fp\3\2")
        buf.write("\2\2\u0170\u0171\t\20\2\2\u0171r\3\2\2\2\u0172\u0173\t")
        buf.write("\21\2\2\u0173t\3\2\2\2\u0174\u0175\t\22\2\2\u0175v\3\2")
        buf.write("\2\2\u0176\u0177\t\23\2\2\u0177x\3\2\2\2\u0178\u0179\t")
        buf.write("\24\2\2\u0179z\3\2\2\2\u017a\u017b\t\25\2\2\u017b|\3\2")
        buf.write("\2\2\u017c\u017d\t\26\2\2\u017d~\3\2\2\2\u017e\u017f\t")
        buf.write("\27\2\2\u017f\u0080\3\2\2\2\u0180\u0181\t\30\2\2\u0181")
        buf.write("\u0082\3\2\2\2\u0182\u0183\t\31\2\2\u0183\u0084\3\2\2")
        buf.write("\2\u0184\u0185\t\32\2\2\u0185\u0086\3\2\2\2\u0186\u0187")
        buf.write("\t\33\2\2\u0187\u0088\3\2\2\2\u0188\u0189\t\34\2\2\u0189")
        buf.write("\u008a\3\2\2\2\u018a\u018b\t\35\2\2\u018b\u008c\3\2\2")
        buf.write("\2\u018c\u018d\t\36\2\2\u018d\u008e\3\2\2\2\u018e\u018f")
        buf.write("\t\37\2\2\u018f\u0090\3\2\2\2\u0190\u0191\t \2\2\u0191")
        buf.write("\u0092\3\2\2\2\u0192\u0193\t!\2\2\u0193\u0094\3\2\2\2")
        buf.write("\u0194\u0195\t\"\2\2\u0195\u0096\3\2\2\2\16\2\u00b4\u00b6")
        buf.write("\u00c3\u00c7\u00ce\u0146\u0148\u014f\u0156\u0158\u015e")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class YAPLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    OPEN_COMMENT = 11
    CLOSE_COMMENT = 12
    COMMENT = 13
    ONE_LINE_COMMENT = 14
    WHITESPACE = 15
    CLASS = 16
    INHERITS = 17
    TRUE = 18
    FALSE = 19
    ASSIGNMENT = 20
    IF = 21
    ELSE = 22
    THEN = 23
    FI = 24
    WHILE = 25
    LOOP = 26
    POOL = 27
    LET = 28
    IN = 29
    CASE = 30
    OF = 31
    ESAC = 32
    CASEARR = 33
    NEW = 34
    ISVOID = 35
    ADD = 36
    MINUS = 37
    MULT = 38
    DIV = 39
    NOT = 40
    LT = 41
    LE = 42
    EQ = 43
    TYPE = 44
    STR = 45
    ID = 46
    INT = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'{'", "'}'", "'('", "','", "')'", "':'", "'@'", "'.'", 
            "'~'", "'(*'", "'*)'", "'<-'", "'=>'", "'+'", "'-'", "'*'", 
            "'/'", "'<'", "'<='", "'='" ]

    symbolicNames = [ "<INVALID>",
            "OPEN_COMMENT", "CLOSE_COMMENT", "COMMENT", "ONE_LINE_COMMENT", 
            "WHITESPACE", "CLASS", "INHERITS", "TRUE", "FALSE", "ASSIGNMENT", 
            "IF", "ELSE", "THEN", "FI", "WHILE", "LOOP", "POOL", "LET", 
            "IN", "CASE", "OF", "ESAC", "CASEARR", "NEW", "ISVOID", "ADD", 
            "MINUS", "MULT", "DIV", "NOT", "LT", "LE", "EQ", "TYPE", "STR", 
            "ID", "INT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "OPEN_COMMENT", "CLOSE_COMMENT", 
                  "COMMENT", "ONE_LINE_COMMENT", "WHITESPACE", "CLASS", 
                  "INHERITS", "TRUE", "FALSE", "ASSIGNMENT", "IF", "ELSE", 
                  "THEN", "FI", "WHILE", "LOOP", "POOL", "LET", "IN", "CASE", 
                  "OF", "ESAC", "CASEARR", "NEW", "ISVOID", "ADD", "MINUS", 
                  "MULT", "DIV", "NOT", "LT", "LE", "EQ", "TYPE", "STR", 
                  "ID", "INT", "A", "B", "C", "D", "E", "F", "G", "H", "I", 
                  "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
                  "U", "V", "W", "X", "Y", "Z", "BACK" ]

    grammarFileName = "YAPL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


