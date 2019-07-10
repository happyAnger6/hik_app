import struct
import ctypes

from hik_app.utils.clib import clib

class XMLCFG_LIPC_RECV_DATA_S:
    _fields_ = [
        ('pcRecvString', ctypes.c_char_p),
        ('uiRestStatus', ctypes.c_uint),
        ('bIsLast', ctypes.c_bool),
    ]

RECVFUNC = ctypes.CFUNCTYPE(ctypes.c_ulong, ctypes.c_void_p, ctypes.c_void_p)

class XmlcfgLipcSendData(ctypes.Structure):
    _fields_ = [
        ('enRestMethodType', ctypes.c_uint),
        ('enNetconfOperation', ctypes.c_uint),
        ('enNetconfEditOperation', ctypes.c_uint),
        ('pcUrlOrXpath', ctypes.c_char_p),
        ('pcSendContent', ctypes.c_char_p),
        ('pUserData', ctypes.c_char_p),
        ('pfRecv', ctypes.c_void_p)
                ]

def XMLCFG_LIPC_ClientInit(uiNetconfFlag,
                           enLipcReqType,
                           enOutputType,
                           pcRolelist,
                           usRoleListLen):
    cfunc = clib.xmlcfg.XMLCFG_LIPC_ClientInit
    cfunc.restype = ctypes.c_ulong
    cfunc.argtypes = (ctypes.c_uint,
                      ctypes.c_uint,
                      ctypes.c_uint,
                      ctypes.c_char_p,
                      ctypes.c_ushort)
    return cfunc(uiNetconfFlag, enLipcReqType,
          enOutputType, pcRolelist, usRoleListLen)

def XMLCFG_LIPC_EpollProc(hXmlcfgHandle):
    cfunc = clib.xmlcfg.XMLCFG_LIPC_EpollProc
    cfunc.restype = ctypes.c_ulong
    cfunc.argtypes = (ctypes.c_ulong)
    return cfunc(hXmlcfgHandle)

