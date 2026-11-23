import CNNImageCodec as codec

codec.LoadModel = 0
codec.epochs = 200

codec.ImageCodecModel(
    codec.trainfolder,
    trainwithnoise=1,
    btrain=2,
)